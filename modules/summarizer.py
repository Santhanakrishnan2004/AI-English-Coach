import os
import google.generativeai as genai
from datetime import datetime
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_session(conversation):
    # Join conversation as role: message
    joined_text = "\n".join([f"{x['role']}: {x['content']}" for x in conversation])

    summary_prompt = f"""
Summarize this English speaking practice session.
Provide:
1. Overall summary of topics
2. Grammar and fluency feedback
3. Vocabulary suggestions
4. Encouraging message

Conversation:
{joined_text}
"""

    response = model.generate_content(summary_prompt)
    summary = response.text.strip()

    # Ensure transcripts folder exists
    os.makedirs("transcripts", exist_ok=True)

    # Create timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"transcripts/session_summary_{timestamp}.txt"

    # Save summary to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== Session Summary ===\n\n")
        f.write(summary)

    print(f"✅ Summary saved to {filename}")
    return summary
