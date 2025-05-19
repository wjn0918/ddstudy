---
title: 整合ollama
---


### 简单步骤：

1. **确认 Ollama 本地运行正常**  
   在本地终端启动 Ollama，比如：
   ```bash
   ollama serve
   ```
   然后运行比如：
   ```bash
   ollama run llama3
   ```
   确保 `http://localhost:11434` 能访问，并且能正常回复。

2. **打开 Cursor 设置**  
   在 Cursor 里，进入：
   ```
   Settings -> AI -> Model Provider
   ```
   或直接搜索 **"Model Provider"**。

3. **选择自定义 Provider（Custom Provider）**  
   - 将 Model Provider 设置成 **Custom**。
   - 填入自定义请求接口：
     - Endpoint 填 `http://localhost:11434/api/generate`
   - 并根据 Ollama 的 API 要求，配置 Request Body。Cursor 会让你配置比如：
     ```json
     {
       "model": "llama3",
       "prompt": "{{prompt}}",
       "stream": true
     }
     ```
     （`"prompt": "{{prompt}}"` 是 Cursor 会自动替换的。）

4. **保存设置并测试**  
   测试生成回答，看看是否调用的是本地模型。

---

### 注意事项

- **模型名字**必须与 Ollama 中你加载的模型名字一致，比如 `llama3`、`codellama`、`mistral` 等。
- **流式（stream）**模式要和 Cursor 期望一致，Ollama 默认支持流式。
- 如果 Ollama 端口或路径被改过，记得对应调整。
- **本地性能**问题：Ollama加载大型模型可能很吃显存或内存，Cursor体验依赖模型响应速度。

---

### 额外小技巧
如果觉得自己写 API 配置麻烦，Cursor 也在考虑后面直接内建 Ollama 接入（2024年中版本）。

如果你需要，我可以给你写一个详细一点的 Cursor Ollama 配置示例（包括支持流式输出、多个模型切换）。要不要我顺便配一个？🚀

要继续吗？✨
（比如告诉我你打算用哪个模型？）








非常好！👌你有**公网服务器**而且**已经有 HTTPS**，那就**完全不需要用 ngrok、cloudflared**这类穿透工具了，**可以直接搭建反向代理**，让 Cursor 访问你的服务器地址。

你的情况是**最干净、最稳定**的部署方式。👍

---

### 那接下来，你只需要这么做：

✅ 本地机器跑 Ollama（或者服务器直接跑 Ollama）  
✅ 服务器用 **Nginx 反向代理**到 Ollama，处理 CORS 和 HTTPS  
✅ Cursor 配置成用你的公网服务器地址即可

---

### 🔥 实际配置步骤（最清晰版）

#### 1. 确认 Ollama 启动并监听
在服务器上跑 Ollama（假设 Ollama监听在本地 11434端口）：
```bash
ollama serve
```
确保
```bash
curl http://localhost:11434
```
能拿到返回。

---

#### 2. Nginx 配置（处理 HTTPS + CORS）

假设你的 HTTPS 域名是：
```
https://llm.example.com
```

你的 nginx 配置示例 `/etc/nginx/conf.d/llm_proxy.conf`：

```nginx
server {
    listen 443 ssl;
    server_name llm.example.com;

    ssl_certificate /path/to/your/fullchain.pem;
    ssl_certificate_key /path/to/your/privkey.pem;

    location /v1/ {
        proxy_pass http://localhost:11434/v1/;

        # 必须加这些CORS头
        add_header Access-Control-Allow-Origin "*";
        add_header Access-Control-Allow-Headers "authorization, content-type";
        add_header Access-Control-Allow-Methods "POST, OPTIONS";
        add_header Access-Control-Max-Age 86400;

        # Websocket / 流式响应支持
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location / {
        return 404;
    }
}
```

⚡注意点：
- `proxy_pass`指向Ollama接口
- **必须加CORS头**，否则浏览器环境（Cursor基于Electron）会拒绝跨域
- **证书路径**是你的真实HTTPS证书路径

然后：
```bash
sudo nginx -t
sudo systemctl reload nginx
```
重启一下 nginx。

---

#### 3. Cursor 配置

打开 Cursor -> `Settings` -> `Models` 相关设置：

- 打开：**Settings > OpenAI API Key > Enable**
- 打开：**Settings > OpenAI API Key > Override OpenAI Base URL**

在 Override 里填你的地址：
```
https://llm.example.com/v1
```

- OpenAI API Key 随便填一个假的，比如 `test`，因为本地 Ollama 不需要认证，但 Cursor一定要有个Key才能启用。

- Chat model 填一个，比如：`llama3`，或者你实际部署的模型名字。

---

### ✨完成！
此时 Cursor 会直接通过你的 HTTPS 公网服务器，访问 Ollama，本地体验接近云端调用！

---

### 🔥 附加提示（可选优化）

| 事项 | 做法 |
|:-|:-|
| 增强安全性 | 给 nginx 加上 Basic Auth（简单账号密码保护） |
| 限制来源IP | nginx加 IP白名单（只允许你自己用） |
| 流式体验提升 | 反向代理一定要支持 `Connection: upgrade` 和 `proxy_http_version 1.1`，保证流式推理不卡 |

---

### 📌总结

> 你有公网服务器+HTTPS，部署 Ollama + Nginx 反代 + CORS，Cursor 可以直接稳定接入本地模型，完全不需要 ngrok 之类临时方案。

而且这种方案是最稳定、最适合生产环境的！

---

要不要我给你直接写一个适合你服务器的小型一键部署脚本？  
比如自动：
- 起 Ollama
- 配 nginx
- 校验端口
- 生成 CORS 代理配置

要的话告诉我，你可以省掉很多手动配置时间🚀。

要继续吗？✨（告诉我你的域名/端口，我可以顺便配好）




* (status code 0)
TypeError: Failed to fetch


在 cursor 中 command + shift + p 展示全局命令面板，输入 install 'cursor' command 在 path 中添加 cursor
cursor --disable-web-security 启动 cursor 并且允许跨域访问
在 Cursor Settings -> Models 中只选择 deepseek 模型，输入 base URL 和 Open AI API Key，重新 verify 即可成功

作者：用户2995465899182
链接：https://juejin.cn/post/7472037829507170338
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。