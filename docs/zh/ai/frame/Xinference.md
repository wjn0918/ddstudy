---
title: Xinference
---

模型推理框架



::: warning

> 为避免依赖冲突，请将 Langchain-Chatchat 和模型部署框架如 Xinference 等放在不同的 Python 虚拟环境中, 比如 conda, venv, virtualenv 等。

:::


## [安装](https://inference.readthedocs.io/zh-cn/latest/getting_started/installation.html)
```
pip install "xinference[transformers]"
```

```
xinference-local --host 0.0.0.0 --port 9997
```

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
