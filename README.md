# 🤖 LangChain Bangla

[![Bangla](https://img.shields.io/badge/UI-Bangla%20%2B%20English-orange)](#)

**A small Bangla AI chat app with conversation memory, plus a Bangla summariser — runs 100% locally on Ollama, no API key, no bill.**

> বাংলা সংস্করণ নিচে আছে। / Bangla version below.

## ✨ Features

- `bangla_chat.py` — terminal chat in Bangla: Bangla prompt template + local Ollama model (`qwen2.5:7b`) + conversation memory, so follow-ups work ("আরও বিস্তারিত বলো") instead of each message starting from zero. The model is created once and reused. Type `quit`, `exit` or `বিদায়` to leave.
- `bangla_summarizer.py` — summarise any text in Bangla: one-line headline, up to 5 short bullet points with the key facts, one line on why it matters. Takes a text file or reads from stdin.
- `requirements.txt` — the packages needed (`langchain`, `langchain-ollama`, `langchain-core`).
- Also included in the chat script: a one-shot `summarise()` function for use from your own code.

## 🚀 How to use

```bash
# 1. Install Ollama and pull the model
ollama pull qwen2.5:7b
ollama serve   # keep running in another terminal

# 2. Install the Python packages
pip install -r requirements.txt

# 3. Chat in Bangla (type 'quit' to exit)
python3 bangla_chat.py

# 4. Or summarise a file
python3 bangla_summarizer.py my-article.txt
echo "বাংলা লেখা..." | python3 bangla_summarizer.py
```

Example:

```
আপনি: বাংলাদেশের জাতীয় মাছ কোনটি?
সহকারী: বাংলাদেশের জাতীয় মাছ ইলিশ।
```

## ⚠️ Honest limits

- You need Ollama running locally with the `qwen2.5:7b` model — this repo is the example app, not the model or the server.
- Answers come from a 7B local model: good for everyday Bangla chat and summaries, but it can be wrong — it says so in Bangla instead of guessing when it does not know.
- The summariser keeps it short by design (headline + up to 5 bullets); it does not keep every detail of a long text.

## 🇧🇩 বাংলা

**LangChain বাংলা — বাংলায় চলা ছোট AI অ্যাপ।**

- `bangla_chat.py` — টার্মিনাল চ্যাট: বাংলা প্রশ্নের বাংলা উত্তর, আগের কথা মনে রাখে।
- `bangla_summarizer.py` — যেকোনো লেখার বাংলা সারাংশ দেয় (শিরোনাম + মূল কথা)।
- লোকাল Ollama (`qwen2.5:7b`) দিয়ে চলে — কোনো key লাগে না, কোনো বিল আসে না।

## 📄 License

MIT — use it however you like; credit is appreciated.
