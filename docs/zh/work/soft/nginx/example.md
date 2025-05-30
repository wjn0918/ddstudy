---
title: 案例
icon: lightbulb
---
## 代理vite 

base: '/easybd',

```

server {
  listen 80;

  server_name localhost;

 location /easybd {
    alias /usr/share/nginx/html;
    index  index.html index.htm;
    #若不配置try_files，刷新会404
    try_files $uri $uri/ /easybd/index.html; # 注意这里需要加上base路径
  }

}

```


## 代理vue

```
export default defineUserConfig({
  base: "/ddstudy/",

  lang: "zh-CN",

  theme,

  // Enable it with pwa
  // shouldPrefetch: false,
});

```

```
server {
     listen 5066; 
     server_name localhost; 
     location ^~ /ddstudy {
     alias /home/soft/schooletl/dist;
     index index.html index.htm;
     }
     location /api {
        proxy_pass http://127.0.0.1:5002;
        proxy_set_header Host $host;
    }

 }

```

## 代理数据库
:::tabs
@tab pgsql

```
# 需要放在nginx.conf 最后

stream {

    upstream cloudsocket {
       hash $remote_addr consistent;
      # $binary_remote_addr;
       server db:5432 weight=5 max_fails=3 fail_timeout=30s;
    }
    server {
       listen 9080;#数据库服务器监听端口
       proxy_connect_timeout 10s;
       proxy_timeout 300s;#设置客户端和代理服务之间的超时时间，如果5分钟内没操作将自动断开。
       proxy_pass cloudsocket;
    }
}
```

@tab mysql

```
#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       81;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

  
    }
}

stream {

    upstream cloudsocket {
       hash $remote_addr consistent;
      # $binary_remote_addr;
       server 数据库IP:数据库地址 weight=5 max_fails=3 fail_timeout=30s;
    }
    server {
       listen 80;#数据库服务器监听端口
       proxy_connect_timeout 10s;
       proxy_timeout 300s;#设置客户端和代理服务之间的超时时间，如果5分钟内没操作将自动断开。
       proxy_pass cloudsocket;
    }
}




```

:::

## 代理目录

```
    location / {
        root /data/EMR;
        autoindex on;
    }
```

```
location / {
        root  /home/shingi/soft/web/dist;
        index  index.html index.htm;
        try_files $uri /index.html;
    }
  location ^~ /api/  {
        set  $proxy_method $request_method;
        if ( $http_x_custommethod != '') {
        set  $proxy_method $http_x_custommethod;
        }
        
        proxy_method $proxy_method;
        proxy_pass http://localhost:10100;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }

   location ^~ /api/fastapi/  {  
        proxy_pass   http://localhost:3302/api/fastapi/;
    }
```


## 代理jupyter notebook
生成配置文件
jupyter notebook --generate-config 
设置密码
jupyter notebook password
更改 .jupyter/jupyter_notebook_config.py
c.ServerApp.base_url = '/nb/'


代理
```
location /nb {
        proxy_pass http://172.25.101.28:10088/nb;
        proxy_set_header Host $host:$server_port;
        proxy_set_header X-Real-Scheme $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_read_timeout 120s;
        proxy_next_upstream error;
        proxy_redirect off;
        proxy_buffering off;
    }


```

## basic认证
```
1. 生成一个账户密码文件 pass_file
htpasswd -c -d /etc/nginx/conf.d/pass_file fd

fd ---用户名

2. nginx.conf

auth_basic "need user and password";
auth_basic_user_file /etc/nginx/conf.d/pass_file;

实例
```
location / {
    auth_basic "need user and password";
    auth_basic_user_file /etc/nginx/conf.d/pass_file;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
}
```