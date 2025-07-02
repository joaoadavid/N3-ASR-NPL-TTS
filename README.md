# 🗣️ Demo ASR + TTS em Python

Este projeto demonstra um pipeline local e offline de:

- **ASR (Reconhecimento automático de fala)** usando Whisper
- **TTS (Síntese de fala)** usando pyttsx3
- Interface web via Gradio para gravar, transcrever e falar quantas vezes quiser

---

## 🚀 Tecnologias utilizadas

| Tecnologia | Finalidade                          |
|------------|------------------------------------|
| Python     | Linguagem principal                |
| Gradio     | Interface web interativa           |
| Whisper    | Transcrição (ASR)                  |
| pyttsx3    | Texto-para-fala (TTS)              |
| NumPy/SciPy| Manipulação de áudio               |
| Torch      | Backend para Whisper               |
| FFmpeg     | Conversão e normalização do áudio  |

---

## ⚙️ Como instalar e executar

### 1. Clone o projeto
```bash
git clone https://github.com/seuusuario/demo-asr-tts.git
cd demo-asr-tts

### 2. Clone o projeto
pip install openai-whisper
pip install gradio
pip install numpy scipy
pip install pyttsx3

### 3. Instale as dependências Python manualmente
bash
Copy
Edit
pip install openai-whisper
pip install gradio
pip install numpy scipy
pip install pyttsx3

### 🎧 4. Baixe e configure o FFmpeg
✅ Baixe o FFmpeg em:

👉 https://www.gyan.dev/ffmpeg/builds/

Baixe o arquivo ffmpeg-git-essentials.7z (ou similar)
Extraia o conteúdo em algum local do seu sistema. Você verá uma pasta com:

bin/
doc/
presets/
Dentro de bin ficam os executáveis ffmpeg.exe e ffprobe.exe.

✅ Adicione o bin do FFmpeg ao PATH:
No Windows, vá em:

Painel de Controle -> Sistema -> Configurações avançadas -> Variáveis de Ambiente
No campo Path, adicione o caminho para o diretório bin, por exemplo:

makefile
Copy
Edit
C:\Users\SeuUsuario\Downloads\ffmpeg-2025-06-28-git-cfd1f81e7d\bin
✅ Para testar, abra o CMD e digite:

ffmpeg -version
Ele deve exibir algo como:
ffmpeg version n6.1.1 ...


### 🚀 5. Execute o projeto

python main.py
Acesse no navegador:
http://127.0.0.1:7860
