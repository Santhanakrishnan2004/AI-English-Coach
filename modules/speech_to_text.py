# modules/speech_to_text.py
import sounddevice as sd
import numpy as np
import whisper
import wave
import os
from config import RECORD_DIR, WHISPER_MODEL

os.makedirs(RECORD_DIR, exist_ok=True)

model = whisper.load_model(WHISPER_MODEL)

def record_audio(duration=5, filename="temp.wav", samplerate=16000):
    print("🎤 Recording... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype="int16")
    sd.wait()
    
    path = os.path.join(RECORD_DIR, filename)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    return path

def transcribe_audio(filepath):
    print("🔍 Transcribing with Whisper...")
    result = model.transcribe(filepath)
    return result["text"]
