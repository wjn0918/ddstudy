---
title: docker 配置
---


## 国内镜像

```
vi /etc/docker/daemon.json
```
- 新增
```
{"registry-mirrors": ["https://dockerproxy.cn"]}
```
- 重载systemd管理守护进程配置文件

```
sudo systemctl daemon-reload
```

- 重启服务

```
sudo systemctl restart docker
```



## migrate docker data directory

- Stop the Docker daemon.

```
systemctl stop docker
```

- Move the existing Docker data directory to the new location.

```
cp -a /usr/local/docker/. /home/docker/
```

- Start the Docker daemon with the --data-root option pointing to the new location.

```
vi /etc/docker/daemon.json
```
```
{
  "data-root": "/home/docker"
}
```




## 所有用户使用

groupadd docker
usermod -aG docker shingi
newgrp docker
