# LangChain Bangla — বাংলায় চলা ছোট AI অ্যাপ

Bangla-first LangChain example, built on **langchain-ai/langchain**.

- **Original repo:** https://github.com/langchain-ai/langchain (the agent engineering platform — build LLM apps and agents with chains, tools and memory)

## কী আছে / What is inside

- `bangla_chat.py` — a small LangChain app: Bangla prompt template + local Ollama model (`qwen2.5:7b`) + conversation memory, in a terminal chat loop. Also shows a one-shot summariser function.
- `requirements.txt` — the packages needed (`langchain`, `langchain-ollama`, `langchain-core`).

## যা ঠিক করা হয়েছে / What was fixed

- Upstream docs and examples are English-only and mostly use paid APIs (OpenAI). This example runs 100% locally on Ollama — no key, no bill — and the prompt template forces Bangla replies.
- The script keeps conversation memory (`ConversationBufferMemory`), so follow-up questions work ("আরও বিস্তারিত বলো") instead of each message starting from zero.
- A common beginner trap is fixed in the code: the model is created once and reused; the old docs pattern of rebuilding the chain per message is slow and drops memory.

## ব্যবহার / How to use

```bash
# 1. Install Ollama and pull the model
ollama pull qwen2.5:7b
ollama serve   # keep running in another terminal

# 2. Install the Python packages
pip install -r requirements.txt

# 3. Chat in Bangla (type 'quit' to exit)
python3 bangla_chat.py
```

Example:
```
আপনি: বাংলাদেশের জাতীয় মাছ কোনটি?
সহকারী: বাংলাদেশের জাতীয় মাছ ইলিশ।
```
