---
title: miniconda
---



- 下载安装脚本
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
```
- 安装
```
bash miniconda.sh -b -u -p /home/miniconda3
```
- 初始化
```
source /home/miniconda3/bin/activate
conda init --all
```