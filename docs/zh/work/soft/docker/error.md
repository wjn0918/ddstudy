---
title: Q&A
---

* Unknown option overlay2.override_kernel_check: devicemapper

更改配置文件/etc/docker/daemon.json 移除overlay2 相关内容
docker daemon
systemctl restart docker 


* cgroup mountpoint does not exist: unknown

sudo mkdir /sys/fs/cgroup/systemd
sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd