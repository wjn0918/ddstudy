---
title: conda
---

# windows

bin/conda.bat activate stablediffusion



conda install -c conda-forge conda-pack
conda pack -n envsname -o conda_envsname.tar.gz

# 单个安装
下载
pip download [packages] -d ./
安装
for i in `ls`; do pip install $i; done