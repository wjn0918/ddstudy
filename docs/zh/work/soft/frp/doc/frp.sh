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