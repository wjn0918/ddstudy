---
title: 配置
icon: gear
---


## 开机自启

nginx.service

cp nginx.service /usr/lib/systemd/system/
systemctl daemon-reload
systemctl enable nginx.service
systemctl start nginx.service

```
[Unit] 
Description=nginx - high performance web server 
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
PIDFile=/data/nginx/logs/nginx.pid
LimitNOFILE=100000
LimitNPROC=65535
LimitMEMLOCK=infinity
ExecStartPre=/opt/third/nginx/sbin/nginx -t -c /opt/third/nginx/conf/nginx.conf
ExecStart=/opt/third/nginx/sbin/nginx -c /opt/third/nginx/conf/nginx.conf
ExecReload=/opt/third/nginx/sbin/nginx -s reload
ExecStop=/opt/third/nginx/sbin/nginx -s stop
ExecQuit=/opt/third/nginx/sbin/nginx -s quit
PrivateTmp=true
Restart=on-failure
RestartSec=40

[Install]
WantedBy=multi-user.target     

```





## https

```
openssl genpkey -algorithm RSA -out ./private.key


openssl req -new -key ./private.key -out ./certificate.csr

openssl x509 -req -in ./certificate.csr -signkey ./private.key -out ./certificate.crt


hingi@2023


ssl_certificate    ./ssl/certificate.crt;
ssl_certificate_key  ./ssl/private.key;

```



## 重定向添加端口

```
server {
       listen 80;
       server_name sx.fdstack.com;
       location / {
          rewrite .* http://$host:9100/ent/index.html permanent;
       }
   }
```







## 高可用

::: tabs

@tab zookeeper



```
from kazoo.client import KazooClient
from kazoo.recipe.election import Election
import os
import time

zk = KazooClient(hosts='192.168.1.1:2181,192.168.1.2:2181')  # Zookeeper 集群地址
zk.start()

election = Election(zk, "/nginx-master")

def run_as_master():
    print("I am the leader now, starting Nginx...")
    os.system("systemctl start nginx")
    while True:
        time.sleep(5)  # 保持主节点状态

def stop_nginx():
    print("I am not the leader, stopping Nginx...")
    os.system("systemctl stop nginx")

@zk.DataWatch("/nginx-master")
def watch_node(data, stat):
    if stat and data:
        print("Another leader is active.")
        stop_nginx()

# 参与选举
election.run(run_as_master)


```


@tab keepalived

https://www.cnblogs.com/wenxuehai/p/15013654.html


:::