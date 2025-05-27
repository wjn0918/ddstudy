---
title: Audio
---

<Catalog/>

```
paraformer
chatgpt
bert
vits
ue5



pyinstaller SockerServer.spec


ImportError: DLL load failed while importing onnxruntime_pybind11_state: 找不到指定的模块。
onnxruntime==1.12.0


DLL load failed while importing _win32sysloader: 找不到指定的模块
pip uninstall pywin32
pip install pywin32



digital_life_server
rapidasr
vits


pip install monotonic_align -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# ubuntu 

sudo apt-get install portaudio19-dev python-all-dev python3-all-dev

移除 WMI==1.5.1


# SentimentEngine.py 更改

#模型下载
from modelscope import snapshot_download
import os
os.environ['MODELSCOPE_CACHE']= '/home/shingi/ai/models'
model_dir = snapshot_download('tiansz/bert-base-chinese')

self.tokenizer = BertTokenizer.from_pretrained(model_dir)


```
