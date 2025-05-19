---
title: network
---

## 容器间访问

curl http://server1:8000

server1 - 是服务名 不是container_name

```
services:
  server1:
    image: python:3.10.15
    container_name: server1
    working_dir: /
    networks:
      - demo
    command: python3 -m http.server
    

  server2:
    image: python:3.10.15
    container_name: server2
    working_dir: /
    networks:
      - demo
    command: tail -f /dev/null
    
networks:
  demo:

```