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




## digital life server 

### 安装

::: tabs

@tab ubuntu
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

pip install torch torchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


:::




## funasr

### 实时版
https://github.com/modelscope/FunASR/blob/main/runtime/docs/SDK_advanced_guide_online_zh.md

sudo docker pull \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.12
mkdir -p ./funasr-runtime-resources/models
sudo docker run -p 10096:10095 -it --privileged=true \
  -v $PWD/funasr-runtime-resources/models:/workspace/models \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.12


 cd FunASR/runtime
nohup bash run_server_2pass.sh \
  --download-model-dir /workspace/models \
  --vad-dir damo/speech_fsmn_vad_zh-cn-16k-common-onnx \
  --model-dir damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-onnx  \
  --online-model-dir damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-online-onnx  \
  --punc-dir damo/punc_ct-transformer_zh-cn-common-vad_realtime-vocab272727-onnx \
  --lm-dir damo/speech_ngram_lm_zh-cn-ai-wesp-fst \
  --itn-dir thuduj12/fst_itn_zh \
  --hotword /workspace/models/hotwords.txt > log.txt 2>&1 &

# 如果您想关闭ssl，增加参数：--certfile 0
# 如果您想使用SenseVoiceSmall模型、时间戳、nn热词模型进行部署，请设置--model-dir为对应模型：
#   iic/SenseVoiceSmall-onnx
#   damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-onnx（时间戳）
#   damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404-onnx（nn热词）
# 如果您想在服务端加载热词，请在宿主机文件./funasr-runtime-resources/models/hotwords.txt配置热词（docker映射地址为/workspace/models/hotwords.txt）:
#   每行一个热词，格式(热词 权重)：阿里巴巴 20（注：热词理论上无限制，但为了兼顾性能和效果，建议热词长度不超过10，个数不超过1k，权重1~100）
# SenseVoiceSmall-onnx识别结果中“<|zh|><|NEUTRAL|><|Speech|> ”分别为对应的语种、情感、事件信息 



python3 funasr_wss_client.py --host "127.0.0.1" --port 10096 --mode 2pass


### 离线版

https://github.com/modelscope/FunASR/blob/main/runtime/docs/SDK_advanced_guide_offline_zh.md

sudo docker pull \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-cpu-0.4.6
mkdir -p ./funasr-runtime-resources/models
sudo docker run -p 10095:10095 -it --privileged=true \
  -v $PWD/funasr-runtime-resources/models:/workspace/models \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-cpu-0.4.6