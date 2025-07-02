import whisper
from scipy.io.wavfile import write
import numpy as np

class Transcribe:
    def __init__(self, model):
        self.model = model

    def transcribe(self, audio):
        try:
            if audio is None:
                return "Nenhum áudio fornecido."
            sample_rate, data = audio
            if np.max(np.abs(data)) == 0:
                return "Áudio mudo, nada foi falado."

            data_int16 = np.int16(data / np.max(np.abs(data)) * 32767)
            file_path = "temp.wav"
            write(file_path, sample_rate, data_int16)

            result = self.model.transcribe(file_path)
            text = result.get("text", "").strip()
            return text if text else "Transcrição vazia."
        except Exception as e:
            return f"Erro ao transcrever: {str(e)}"
