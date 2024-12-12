# 保存音频

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