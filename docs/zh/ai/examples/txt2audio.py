import gradio as gr
import librosa
import os

title = "文本转语音"

import asyncio

import websockets

from TTS import TTService
from SentimentEngine import SentimentEngine
import time
import logging


paimon = ['TTS/models/paimon6k.json', 'TTS/models/paimon6k_390k.pth', 'character_paimon', 1]

tts = TTService.TTService(*paimon)
sentiment = SentimentEngine.SentimentEngine('SentimentEngine/models/paimon_sentiment.onnx')
tmp_proc_file = 'tmp/server_processed.wav'
def send_voice(resp_text, senti_or=None):
    tts.read_save(resp_text, tmp_proc_file, tts.hps.data.sampling_rate)
    with open(tmp_proc_file, 'rb') as f:
        senddata = f.read()
    if senti_or:
        senti = senti_or
    else:
        senti = sentiment.infer(resp_text)
    senddata += b'?!'
    senddata += b'%i' % senti
    time.sleep(0.5)
    logging.info('WAV SENT, size %i' % len(senddata))
    return senddata


def generateAudio(text):
    # 由于TTS无法很好地处理回车符和空格，需要对text里的回车符进行替换
    send_voice(text)
    audio, sr = librosa.load(path=tmp_proc_file)

    return sr, audio


app = gr.Interface(
    fn=generateAudio,
    inputs="text",
    outputs="audio",
    title=title,
    examples=[os.path.join(os.path.dirname(__file__), "output.wav")]
)


app.launch(server_name="0.0.0.0")
