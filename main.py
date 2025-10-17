# main.py
from modules.session_manager import start_session
from modules.summarizer import summarize_session

if __name__ == "__main__":
    goal = input("🧠 Enter today's speaking goal: ")
    duration = int(input("⏱️ Enter duration (minutes): "))

    conversation = start_session(goal, duration)
    print("\n📋 Generating summary...\n")
    summary = summarize_session(conversation)
    print(summary)
