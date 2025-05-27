---
title: Xinference
---

模型推理框架



::: warning

> 为避免依赖冲突，请将 Langchain-Chatchat 和模型部署框架如 Xinference 等放在不同的 Python 虚拟环境中, 比如 conda, venv, virtualenv 等。

:::


## [安装](https://inference.readthedocs.io/zh-cn/latest/getting_started/installation.html)
```
conda create -n xinference python==3.10
conda activate xinference
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

pip3 install "xinference" -i https://pypi.tuna.tsinghua.edu.cn/simple
```

```
xinference-local --host 0.0.0.0 --port 9997
```

::: warning

* libgomp.so.1, needed by vendor/llama.cpp/ggml/src/libggml.so, not found

通过查找命令 find /usr -name libgomp.so.1
找到内容 
/usr/lib/x86_64-linux-gnu/libgomp.so.1
 
 
然后在执行安装命令前, 输入如下命令并回车, 指定 LD_LIBRARY_PATH
 export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
 
然后再执行如下命令成功了
pip install "xinference[all]"

* xinference[all] 安装时，默认会把所有【需要GPU加速】的模块都一起安装，所以安装失败了。
只装 CPU 版
pip3 install "xinference" -i https://pypi.tuna.tsinghua.edu.cn/simple

:::


## 设置

XINFERENCE_HOME=/tmp/xinference  # 存储位置
XINFERENCE_MODEL_SRC=modelscope # 指定模型下载网站


## 使用

### 查询与 qwen-chat 模型相关的参数组合
xinference engine -e http://localhost:9997 --model-name qwen-chat

### 使用其他模型托管平台
```
XINFERENCE_MODEL_SRC=modelscope
```
```
xinference-local --host 0.0.0.0 --port 9997
```

访问  http://ip:9997/ui

```
xinference launch --model-engine Transformers -u my-ai -n qwen-chat -s 7 -f pytorch


```
