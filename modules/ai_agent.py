# modules/ai_agent.py
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def get_ai_response(prompt, history=None):
    context = ""
    if history:
        context = "\n".join([f"{x['role']}: {x['content']}" for x in history[-6:]])  # last 6 turns

    full_prompt = f"""
You are an English-speaking coach. Encourage conversation, correct mistakes politely,
and ask engaging follow-up questions.

{context}
User: {prompt}
Assistant:
"""
    response = model.generate_content(full_prompt)
    return response.text.strip()
