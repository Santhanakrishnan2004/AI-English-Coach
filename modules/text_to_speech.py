import subprocess

def speak_text(text):
    # Full path to the espeak-ng executable
    espeak_path = r"C:\Program Files\eSpeak NG\espeak-ng.exe"
    subprocess.run([espeak_path, text])
    
# Test it
if __name__ == "__main__":
    speak_text("Hello Macha, your AI English partner is ready!")
