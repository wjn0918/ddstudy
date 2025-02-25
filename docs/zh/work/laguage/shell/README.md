---
title: Shell
---
<Catalog/>


等待

```
#等待59秒
seconds_left=59
echo "等待服务启动....."
while [ $seconds_left -gt 0 ];do
  echo -n $seconds_left
  sleep 1
  seconds_left=$(($seconds_left - 1))
  echo -ne "\r     \r"   #清除本行文字
done

```