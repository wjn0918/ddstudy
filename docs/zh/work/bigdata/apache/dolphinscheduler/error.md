---
title: Q&A
---
* Failed to write core dump. Core dumps have been disabled. To enable core dumping, try "ulimit -c unlimited" before starting Java again

1、vi /etc/sysctl.conf
设置fs.file-max=655350
vm.max_map_count=655360
保存之后sysctl -p使设置生效
2、vi /etc/security/limits.conf 新增
```
* soft nofile 655350
* hard nofile 655350
```


* 中文乱码

localedef -i en_US -f UTF-8 en_US.UTF-8



* 存储未启用

api-server worker-server common.properties修改，需要核查是否更改的是启动文件

* 创建租户错误

查看resource.hdfs.root.user 配置