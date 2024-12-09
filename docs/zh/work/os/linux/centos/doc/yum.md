yum provides */nc


# 配置本地yum源

* 创建挂载目录

> mkdir -p /data/yumiso

* 挂载镜像
mount -o loop /root/CentOS-7-x86_64-Everything-1611.iso /data/yumiso

* 注释原始yum
> rename repo repo.bak *.repo
* 新增本地yum
> yum-config-manager --add-repo file:///data/yumiso


```
[local]
name=local
baseurl=file:///data/yumiso
enabled=1
gpgcheck=0
```