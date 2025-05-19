---
title: Gradio
---
## 保存音频

```
import gradio as gr
import numpy as np
import soundfile as sf  # 需要安装 soundfile 库来保存音频数据


def save_audio(audio):
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))
    # 保存归一化后的音频数据为 WAV 文件
    sf.write("speak.wav", y, sr)

    return "提交成功"

demo = gr.Interface(
    save_audio,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()


```


```
import gradio as gr

def greet(name):
    prompt_text = f"user\n{name} \n assistant \n"
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
        yield stream_result
    

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.queue()
demo.launch()   

```