#!/usr/bin/env python3
"""Bangla summariser with LangChain + local Ollama (no API key).

Usage:
    python3 bangla_summarizer.py <text-file.txt>
    echo "বাংলা লেখা..." | python3 bangla_summarizer.py
Needs Ollama running locally with qwen2.5:7b (see bangla_chat.py).
"""
import sys

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You summarize text in Bangla. Give: 1) a one-line headline, "
            "2) up to 5 short bullet points with the key facts, "
            "3) one line on why it matters. Simple Bangla, no invented details.",
        ),
        ("user", "{text}"),
    ]
)


def main() -> None:
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    if not text.strip():
        print("কোনো লেখা পাওয়া যায়নি — ফাইল দিন বা stdin-এ লেখা পাঠান।")
        sys.exit(1)
    llm = ChatOllama(model="qwen2.5:7b", temperature=0.3)
    print((PROMPT | llm).invoke({"text": text}).content)


if __name__ == "__main__":
    main()
