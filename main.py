import os
import torch
import whisper
import pyttsx3
import gradio as gr
from scipy.io.wavfile import write
import numpy as np
import threading

os.environ["PATH"] += os.pathsep + os.getcwd()
torch.set_num_threads(8)

model = whisper.load_model("base")

def transcribe(audio):
    try:
        if audio is None:
            return "Nenhum áudio fornecido."
        sample_rate, data = audio
        if np.max(np.abs(data)) == 0:
            return "Áudio mudo, nada foi falado."

        data_int16 = np.int16(data / np.max(np.abs(data)) * 32767)
        file_path = "temp.wav"
        write(file_path, sample_rate, data_int16)

        result = model.transcribe(file_path)
        text = result.get("text", "").strip()
        return text if text else "Transcrição vazia."
    except Exception as e:
        return f"Erro ao transcrever: {str(e)}"

def speak(text):
    def tts_job():
        local_engine = pyttsx3.init()
        local_engine.setProperty('rate', 150)
        local_engine.say(text)
        local_engine.runAndWait()
    threading.Thread(target=tts_job).start()
    return "TTS iniciado."

with gr.Blocks() as demo:
    gr.Markdown("## ASR + TTS Multi Transcrição\nGrave e transcreva quantas vezes quiser.")
    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="numpy", label="Fale algo no microfone")
    transcribe_btn = gr.Button("Transcrever")
    output_text = gr.Textbox(label="Transcrição")

    tts_btn = gr.Button("Falar texto")
    tts_output = gr.Textbox(label="Status TTS")

    transcribe_btn.click(fn=transcribe, inputs=audio_input, outputs=output_text)
    tts_btn.click(fn=speak, inputs=output_text, outputs=tts_output)

demo.launch()
