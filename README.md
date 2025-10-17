
# 📘 AI English Speaking Coach

> Your personal AI speaking companion — speak naturally, get real-time AI replies, and receive a personalized summary with fluency feedback!

---

## 🚀 Features

- 🎤 **Voice Input:** Speak naturally — your voice is transcribed using OpenAI Whisper.  
- 🧠 **AI Response:** Gemini AI analyzes your message and replies contextually.  
- 🗣️ **Text-to-Speech:** eSpeak-NG speaks the AI’s response in real-time.  
- ⏱️ **Timed Sessions:** Set a speaking goal and duration for each session.  
- 📄 **Session Summaries:** Automatically saves grammar feedback, vocabulary tips, and encouragement in `/transcripts`.  

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Speech-to-Text | Whisper |
| AI Model | Google Gemini (`google-generativeai`) |
| Text-to-Speech | eSpeak-NG |
| Language | Python 3.10+ |

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/<your-username>/AI-English-Coach.git
cd AI-English-Coach

# Install dependencies
pip install -r requirements.txt
````

### Add your Gemini API key

In `config.py`:

```python
GEMINI_API_KEY = "your_api_key_here"
```

### Run the app

```bash
python main.py
```

---

## 🗂️ Project Structure

```
AI-English-Coach/
│
├── main.py
├── config.py
│
├── modules/
│   ├── ai_agent.py
│   ├── session_manager.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   └── summarizer.py
│
├── transcripts/
│   └── session_summary_YYYY-MM-DD.txt
│
└── README.md
```

---

## 🌟 Future Improvements

* 🌐 Add a web interface (Streamlit or Next.js)
* 📈 Integrate user progress tracking
* 🌍 Add multi-language speaking modes
* 🗣️ Support different TTS engines for more natural tones

---

## 🧑‍💻 Author

**Santhana Krishnan** — Data Scientist & AI Developer
🚀 Passionate about human–AI communication and applied machine learning.

[![GitHub](https://img.shields.io/badge/GitHub-@SanthanaKrishnan-black?logo=github)](https://github.com/Santhanakrishnan2004/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/santhanakrishnan-v/)


