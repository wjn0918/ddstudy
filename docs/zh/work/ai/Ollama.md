---
title: Ollama
---

Ollama 是一个可以在自己电脑上运行大语言模型（LLMs）的小工具。


## 配置

OLLAMA_HOST 0.0.0.0

netsh advfirewall firewall add rule name="Allow Port 11434" dir=in action=allow protocol=TCP localport=11434



* 启动 

ollama serve


## nginx 代理

```
 location /v1/ {
        # 处理预检请求（OPTIONS）
        if ($request_method = OPTIONS) {
            add_header Access-Control-Allow-Origin "*";
            add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
            add_header Access-Control-Allow-Headers "Authorization, Content-Type";
            return 204;
        }

        # 正式请求走代理
        proxy_pass http://localhost:11434;

        # CORS headers
        add_header Access-Control-Allow-Origin "*";
        add_header Access-Control-Allow-Headers "Authorization, Content-Type";
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
    }

```



## 测试

```
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3",
    "messages": [
      { "role": "system", "content": "You are a helpful assistant." },
      { "role": "user", "content": "Hello!" }
    ]
  }'
```

```
curl https://catpd.cn/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer c4cd6c77-37ee-4d0a-bf55-999e0ffceb88" -d "{ \"messages\": [ { \"role\": \"system\", \"content\": \"You are a test assistant.\" }, { \"role\": \"user\", \"content\": \"Testing. Just say hi and nothing else.\" } ], \"model\": \"llama3\" }"
```

## 错误

(status code 0) TypeError: Failed to fetch


可以正常使用，不受影响



## GPU加速

nvidia-smi 

OLLAMA_GPU_LAYER cuda

CUDA_VISIBLE_DEVICES   GPU-32c44cdf-114a-b09c-0dd0-431d3faa9eab

nvidia-smi -L