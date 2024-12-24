---
title: docker file 案例 
---

[Dockerfile overview](https://docs.docker.com/build/concepts/dockerfile/)

## 构建命令
```
docker build -f Dockerfile* -t imagename .
```


## 基础环境构建

### python
```
# 使用 OpenJDK 8 作为基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:openjdk-8-jre-alpine

RUN apk update && apk add python

CMD ["tail", "-f", "/dev/null"]

```

## java

```
# 使用 OpenJDK 8 作为基础镜像
FROM openjdk:8-jre-alpine

# 设置工作目录，可选
WORKDIR /app

# 将你的 Java 应用程序 JAR 文件添加到容器中
COPY your-java-app.jar app.jar

# 启动 Java 应用程序
CMD ["java", "-jar", "app.jar"]

```

## node

```
From node:18.20.5-alpine

# 设置工作目录，可选
WORKDIR /app

# 将你的 Java 应用程序 JAR 文件添加到容器中
COPY your-java-app.jar app.jar

# 启动 Java 应用程序
CMD ["java", "-jar", "app.jar"]

```



## datax


```
# 使用 OpenJDK 8 作为基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/wjn0918/soft:python-openjdk-8-jre-alpine

# 设置工作目录，可选
WORKDIR /app

# 将你的 Java 应用程序 JAR 文件添加到容器中
COPY ./datax /app

# 启动 Java 应用程序
CMD ["tail", "-f", "/dev/null"]

```
