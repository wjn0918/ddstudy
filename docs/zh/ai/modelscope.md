---
title: modelscope
---


https://github.com/modelscope/modelscope-agent/blob/master/examples/llms/local_llm.ipynb

## 模型下载
```
import os
# 设置模型缓存路径
os.environ['MODELSCOPE_CACHE'] = r'D:\wjn\models'

from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('qwen/Qwen-7B-Chat')
```



## transformers-stream-generator

https://github.com/LowinLi/transformers-stream-generator




```
from transformers import AutoTokenizer, TextGenerationPipeline, TextStreamer, GenerationConfig
import torch
from transformers_stream_generator import init_stream_support
init_stream_support()



def tulu_prompt(input):
        return f'''### Human: {input}
### Assistant:'''

from transformers_stream_generator import init_stream_support
init_stream_support()

### Assistant:'''

text = "写一个励志的故事"

tokens = tokenizer(tulu_prompt(input=text), return_tensors="pt", add_special_tokens=False).input_ids.cuda()

generator = (model.generate(inputs=tokens, max_new_tokens=256, temperature=0.5, top_k=35, top_p=0.90, do_sample=True, do_stream=True))

for token in generator:
    word = tokenizer.decode(token)
    print(word, end='', flush=True)
```




https://github.com/lyhue1991/torchkeras



```
from copy import deepcopy
generation_config =  deepcopy(model.generation_config)
config_dic = generation_config.to_dict()
config_dic.update({'do_stream':True})
config_dic
stream_config = StreamGenerationConfig(**config_dic)


prompt_text = "user\n输出一则励志故事 \n assistant \n"

input_ids = tokenizer(
    prompt_text, return_tensors="pt", add_special_tokens=False
).input_ids
generator = model.generate(
            input_ids,
            generation_config=stream_config,
            do_sample=True,
        )
stream_result = ""
for x in generator:
    chunk = tokenizer.decode(x, skip_special_tokens=True)
    print(chunk)
    stream_result += chunk

```




https://github.com/QwenLM/Qwen/issues/604


## error

ImportError: cannot import name 'TypeIs' from 'typing_extensions'


pip install typing_extensions==4.12.0