---
title: FRPC 内网穿透
---
## 安装
[下载地址](https://github.com/fatedier/frp/releases)


:::tabs



@tab windows

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