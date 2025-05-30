---
title: docker file 案例 
---

[Dockerfile overview](https://docs.docker.com/build/concepts/dockerfile/)

## 构建命令
```
docker build -f Dockerfile* -t imagename .
```

## COPY排除指定文件

创建.dockerignore  添加需要排除的内容




## 基础环境构建

### python
```
# 使用官方 Python 3 基础镜像
FROM python:3.10.17-slim

# 设置工作目录
WORKDIR /app

# 升级 pip 工具
RUN pip install --upgrade pip setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 复制 requirements 文件并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 复制项目文件
COPY . .

# 暴露端口
EXPOSE 5001

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]


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
