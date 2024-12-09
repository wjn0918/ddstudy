---
title: 安装docker
icon: circle-info
---

## 离线安装

### centos

- 下载docker rpm包

```
yum install -y docker-ce --downloadonly --downloaddir=./
```

::: note
将下载好的安装包上传到服务器
:::




- 安装

```
for item in `ls`; do rpm -Uvh ${item} --force --nodeps; done
```



