---
title: ai
icon: lightbulb
---


## 开源参考

| 项目                                                                                      | 说明 |
| ----------------------------------------------------------------------------------------- | ---- |
| [Langchain-chatchat](https://github.com/chatchat-space/Langchain-Chatchat)                | 可离线部署的 RAG 与 Agent 应用项目 |
| [torchkeras](https://github.com/lyhue1991/torchkeras)                                     |      |
| [transformers-stream-generator](https://github.com/LowinLi/transformers-stream-generator) |      |



## Xinference

::: warning

> 为避免依赖冲突，请将 Langchain-Chatchat 和模型部署框架如 Xinference 等放在不同的 Python 虚拟环境中, 比如 conda, venv, virtualenv 等。


:::

```
pip install "xinference[transformers]"
```

```
xinference-local --host 0.0.0.0 --port 9997
```



huggingface 国内下载  https://hf-mirror.com/

查看显存  nvidia-smi
watch -n 10 nvidia-smi

vllm
gpu_memory_utilization


pip install -r requirements.txt  --use-pep517

## 本地模型加载

修改 configs/model_config.py




## NLP 


https://github.com/HqWu-HITCS/Awesome-Chinese-LLM





https://github.com/chatchat-space/Langchain-Chatchat/issues/3003
```
from os import * 
from pwd import * 

def get_username():
    return getpwuid(getuid())[0]
```

\Miniconda3\envs\l2\Lib




## 文本分类

* 情感分类
* 零样本分类

## 文本生成

## 完形填空（Fill-Mask）

## 命名实体识别()

## 抽取式问答

## 摘要

## 翻译

只有编码器的模型：擅长自然语言理解任务，例如文本分类和命名实体识别。
只有解码器的模型：擅长自然语言生成任务，例如文本生成。
编码器和解码器或（序列到序列seq2seq）模型：擅长给定输入条件的文本生成任务，例如翻译和摘要。


编码器架构Encoder	ALBERT, BERT, DistilBERT, ELECTRA, RoBERTa	文本分类、命名实体识别和抽取式问答
解码器架构Decoder	CTRL, GPT, GPT-2, Transformer XL	文本生成
Seq2seq架构Encoder-decoder	BART, T5, Marian, mBART	摘要、翻译和生成式问答




ImportError: libGL.so.1: cannot open shared object file: No such file or directory

pip install opencv-python-headless