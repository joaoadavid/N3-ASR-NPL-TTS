import os
import torch
import whisper
import gradio as gr
from transcriber import Transcribe
from speaker import Speak

# Garante ffmpeg local
os.environ["PATH"] += os.pathsep + os.getcwd()
torch.set_num_threads(8)

# Carrega modelo Whisper
model = whisper.load_model("base")

# Instancia classes
transcriber = Transcribe(model)
speaker = Speak()

# Gradio
with gr.Blocks() as demo:
    gr.Markdown("## Demo ASR + TTS Multi Transcrição\nGrave e transcreva quantas vezes quiser.")

    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="numpy", label="Fale algo no microfone")
    transcribe_btn = gr.Button("Transcrever")
    output_text = gr.Textbox(label="Transcrição")

    tts_btn = gr.Button("Falar texto")
    tts_output = gr.Textbox(label="Status TTS")

    transcribe_btn.click(fn=transcriber.transcribe, inputs=audio_input, outputs=output_text)
    tts_btn.click(fn=speaker.speak, inputs=output_text, outputs=tts_output)

demo.launch()
