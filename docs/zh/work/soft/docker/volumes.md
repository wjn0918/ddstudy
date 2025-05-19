---
title: volumes
---


# volumes

https://blog.karakarua.com/2021/04/02/0326889327e6/index.html

## 创建volumes
docker volume create maven_repo -o type=nfs -o device=:$HOME/.m2

## 容器挂载

```
services:
  demo:
    image: maven:3.5.0-alpine
    volumes: 
      - maven_repo:/root/.m2

volumes:
  maven_repo:
```


```
services:
  maven:
    image: maven:3.5.0-alpine
    volumes:
      - ./:/ambari
      - maven_repo:/root/.m2
    working_dir: /ambari
    command: sh -c "mvn clean && tail -f /etc/passwd"

volumes:
  maven_repo:
```