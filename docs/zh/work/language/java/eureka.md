---
title: eureka
---

##  多网卡注册问题
https://blog.csdn.net/liangcha007/article/details/102364767
```
eureka.client.service-url.defaultZone=http://192.168.1.121:7971/eureka/
eureka.instance.ip-address=192.168.1.110
eureka.instance.prefer-ip-address=true
eureka.instance.instance-id=${eureka.instance.ip-address}:${server.port}
```