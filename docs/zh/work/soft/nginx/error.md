---
title: Q&A
icon: lightbulb
---

* 跳转丢失端口

只需要在$host后添加 “:$server_port”即可

proxy_set_header Host $host;
改为
proxy_set_header Host $host:$server_port;



