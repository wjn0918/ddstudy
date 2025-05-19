---
title: Common
---

* Failed to write core dump. Core dumps have been disabled. To enable core dumping, try "ulimit -c unlimited" before starting Java again


问题的根本原因在于服务器的运行应用程序的打开文件的最大数及最大进程数设置的相对较小默认为4096
vi /etc/security/limits.conf

```
* soft nofile 655350
* hard nofile 655350
```
