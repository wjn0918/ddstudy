---
title: docker file 案例 - java
icon: circle-info
---


## hello world

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