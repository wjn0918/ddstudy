---
title: Xinference
---

模型推理框架



::: warning

> 为避免依赖冲突，请将 Langchain-Chatchat 和模型部署框架如 Xinference 等放在不同的 Python 虚拟环境中, 比如 conda, venv, virtualenv 等。

:::


## [安装](https://inference.readthedocs.io/zh-cn/latest/getting_started/installation.html)
```
pip3 install "xinference[all]" -i https://pypi.tuna.tsinghua.edu.cn/simple
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

:::





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

```
xinference launch --model-engine Transformers -u my-ai -n qwen-chat -s 7 -f pytorch


```
