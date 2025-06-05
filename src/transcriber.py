import os

# Força o Python a encontrar o ffmpeg mesmo dentro do venv
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

import whisper

model = whisper.load_model("base")
result = model.transcribe("resources/audio_test1.m4a")
print(result["text"])
