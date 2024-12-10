---
title: 案例
icon: lightbulb
---

## 代理目录

```
    location / {
        root /data/EMR;
        autoindex on;
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