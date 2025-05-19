---
title: Q&A
---

* 用户密码正确还是报错  ERROR RetryUtil - Exception when calling callable, 异常Msg:DataX无法连接对应的数据库，可能原因是：

jdbc后要添加 useSSL=false

* Hive有分区文件到时select不到数据问题-----修复分区命令 msck repair table xxxxx


*  Could not find goal 'assembly' in plugin org.apache.maven.plugins:maven-assembly-plugin:3.4.2 among available goals help, single

maven-assembly-plugin 设置版本
```
<artifactId>maven-assembly-plugin</artifactId>
<version>2.2-beta-5</version>
```