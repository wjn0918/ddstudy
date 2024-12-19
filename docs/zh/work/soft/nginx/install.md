---
title: 安装
icon: lightbulb
---

::: tabs

@tab docker-compose

```
services:
  nginx-1.20.2:
    image: nginx:1.20.2-alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./conf.d:/etc/nginx/conf.d
    network_mode: "host"
```

@tab docker

```
FROM nginx:1.24.0
# 设置工作目录，可选
WORKDIR /app

# 将你的 Java 应用程序 JAR 文件添加到容器中
COPY dist/ /app/dist/

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]

# mkdir -p school-front/conf.d
```

@tab 手动



1. [下载安装包](http://nginx.org/)
2. 解压
3. 安装相关依赖

   yum -y install gcc pcre-devel openssl openssl-devel
4. 编译nginx

   ./configure --prefix=解压到的文件目录（安装目录，不需要创建）  --without-http_rewrite_module --without-http_gzip_module
5. ./configure --prefix=/usr/local/nginx/nginx1.14.2 --without-http_rewrite_module --with-http_gzip_static_module --with-stream --with-pcre 

例：

    ./configure --prefix=/usr/local/nginx/nginx1.6.3 --without-http_rewrite_module --without-http_gzip_module --with-stream

5. 安装

   make install
6. 启动

   * 进入sbin 目录
   * 启动./nginx
   * 关闭 ./nginx -s quit
   * 重启 ./nginx -s reload
7. 创建软连接（可选）

ln  -s  [源文件或目录]  [目标文件或目录]

例:

    ln -s /usr/local/nginx/nginx1.6.3/sbin/nginx /usr/local/bin/nginx

@tab Ubuntu

```
sudo apt install nginx
```

:::