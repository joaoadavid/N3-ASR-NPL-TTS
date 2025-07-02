import pyttsx3
import threading

class Speak:
    def __init__(self):
        pass  # não mantém o engine global

    def speak(self, text):
        def tts_job():
            local_engine = pyttsx3.init()
            local_engine.setProperty('rate', 150)
            local_engine.say(text)
            local_engine.runAndWait()
        threading.Thread(target=tts_job).start()
        return "TTS iniciado."
