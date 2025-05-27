---
title: FunASR
---


[参考](https://github.com/modelscope/FunASR)


## funasr

### [实时版](https://github.com/modelscope/FunASR/blob/main/runtime/docs/SDK_advanced_guide_online_zh.md)

* 拉取镜像

```
sudo docker pull \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.12
```
* 创建模型存储地址
```
mkdir -p ./funasr-runtime-resources/models
```

* 启动容器

```
sudo docker run -p 10096:10095 -it --privileged=true \
  -v $PWD/funasr-runtime-resources/models:/workspace/models \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.12

```

cd FunASR/runtime
nohup bash run_server_2pass.sh \
  --download-model-dir /workspace/models \
  --vad-dir damo/speech_fsmn_vad_zh-cn-16k-common-onnx \
  --model-dir damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-onnx  \
  --online-model-dir damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-online-onnx  \
  --punc-dir damo/punc_ct-transformer_zh-cn-common-vad_realtime-vocab272727-onnx \
  --lm-dir damo/speech_ngram_lm_zh-cn-ai-wesp-fst \
  --itn-dir thuduj12/fst_itn_zh \
  --certfile 0 \
  --hotword /workspace/models/hotwords.txt > log.txt 2>&1 &

```
# 如果您想关闭ssl，增加参数：--certfile 0
# 如果您想使用SenseVoiceSmall模型、时间戳、nn热词模型进行部署，请设置--model-dir为对应模型：
#   iic/SenseVoiceSmall-onnx
#   damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-onnx（时间戳）
#   damo/speech_paraformer-large-contextual_asr_nat-zh-cn-16k-common-vocab8404-onnx（nn热词）
# 如果您想在服务端加载热词，请在宿主机文件./funasr-runtime-resources/models/hotwords.txt配置热词（docker映射地址为/workspace/models/hotwords.txt）:
#   每行一个热词，格式(热词 权重)：阿里巴巴 20（注：热词理论上无限制，但为了兼顾性能和效果，建议热词长度不超过10，个数不超过1k，权重1~100）
# SenseVoiceSmall-onnx识别结果中“<|zh|><|NEUTRAL|><|Speech|> ”分别为对应的语种、情感、事件信息 

```


python funasr_wss_client.py --host "192.168.3.12" --port 10096 --mode 2pass --ssl 0 --audio_in "D:\wjn\gitee\audioC\test.wav"


### 离线版

https://github.com/modelscope/FunASR/blob/main/runtime/docs/SDK_advanced_guide_offline_zh.md

sudo docker pull \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-cpu-0.4.6
mkdir -p ./funasr-runtime-resources/models
sudo docker run -p 10095:10095 -it --privileged=true \
  -v $PWD/funasr-runtime-resources/models:/workspace/models \
  registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-cpu-0.4.6