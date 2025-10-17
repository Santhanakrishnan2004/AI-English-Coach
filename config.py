# config.py
import os

# Load Gemini API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Whisper model size ("tiny", "base", "small", "medium", "large")
WHISPER_MODEL = "base"

# Directory paths
RECORD_DIR = "data/recordings/"
TRANSCRIPT_DIR = "data/transcripts/"
