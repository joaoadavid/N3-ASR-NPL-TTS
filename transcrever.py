import os
import torch
import whisper
import gradio as gr
from scipy.io.wavfile import write
import numpy as np

# Garante ffmpeg local
os.environ["PATH"] += os.pathsep + os.getcwd()

# Otimiza CPU
torch.set_num_threads(8)

# Modelo rápido
model = whisper.load_model("base")

def transcribe(audio):
    try:
        if audio is None:
            return "Nenhum áudio fornecido."

        sample_rate, data = audio

        # Se mudo, evita divisão por zero
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

# Interface Gradio
iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(sources=["microphone"], type="numpy", label="Fale algo no microfone"),
    outputs="text",
    title="Transcrição Automática",
    description="Grave sua voz. O sistema transcreve o que foi falado e exibe abaixo."
)

iface.launch()
