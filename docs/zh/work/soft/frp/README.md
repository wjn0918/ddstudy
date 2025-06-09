---
title: FRPC 内网穿透
---
## 安装
[下载地址](https://github.com/fatedier/frp/releases)


## 开机自启

:::tabs

@tab windows


---


### 步骤：

1. **打开“任务计划程序”**：

   * 按下 `Win + S` 搜索“任务计划程序”或“Task Scheduler”，点击打开。

2. **创建任务**：

   * 点击右侧的【创建基本任务】或【创建任务】（推荐）。
   * 名称如：`Start FRPC`

3. **触发器**：

   * 选择“当计算机启动时” 或 “用户登录时”。

4. **操作**：

   * 选择“启动程序”。
   * 程序或脚本填：

     ```
     C:\wjn\soft\frp_0.61.2_windows_amd64\frpc.exe
     ```
   * 添加参数：

     ```
     -c C:\wjn\soft\frp_0.61.2_windows_amd64\frpc.toml
     ```

5. **权限设置（重要）**：

   * 勾选“使用最高权限运行”。

6. **完成创建任务**，可以在任务计划程序库中看到。

---


:::


## 配置

```

serverAddr = "47.97.35.199"
serverPort = 7000

[[proxies]]
name = "pgsql"
type = "tcp"
localIP = "192.168.3.89"
localPort = 11434
remotePort = 11434
```



## 启动脚本
```
#!/bin/bash

start_frpc() {
  if pgrep -f "./frpc -c frpc_xy.ini"; then
    echo "frpc已经在运行."
  else
    nohup ./frpc -c frpc_xy.ini >/dev/null 2>&1 &
    echo "frpc已启动."
  fi
}

stop_frpc() {
  if pgrep -f "./frpc -c frpc_xy.ini"; then
    pkill -f "./frpc -c frpc_xy.ini"
    echo "frpc已关闭."
  else
    echo "frpc未在运行."
  fi
}

case "$1" in
  "start")
    start_frpc
    ;;
  "stop")
    stop_frpc
    ;;
  *)
    echo "用法: $0 {start|stop}"
    exit 1
    ;;
esac

exit 0
```