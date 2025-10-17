# modules/session_manager.py
import time
from modules.speech_to_text import record_audio, transcribe_audio
from modules.text_to_speech import speak_text
from modules.ai_agent import get_ai_response

def start_session(goal, duration_minutes=2):
    print(f"🎯 Goal: {goal} | Duration: {duration_minutes} min\n")
    end_time = time.time() + duration_minutes * 60
    conversation = []

    while time.time() < end_time:
        filepath = record_audio(duration=5)
        user_text = transcribe_audio(filepath)

        if not user_text.strip():
            continue
        
        conversation.append({"role": "user", "content": user_text})
        ai_reply = get_ai_response(user_text, history=conversation)
        conversation.append({"role": "assistant", "content": ai_reply})

        speak_text(ai_reply)

    return conversation
