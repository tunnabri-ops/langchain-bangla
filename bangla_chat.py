#!/usr/bin/env python3
"""Bangla chat with LangChain + local Ollama (no API key).

Needs Ollama running locally with the qwen2.5:7b model:
    ollama pull qwen2.5:7b
    ollama serve
Then: python3 bangla_chat.py
"""
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

SYSTEM_PROMPT = (
    "You are a helpful assistant for Bengali users. "
    "Always reply in Bangla (বাংলা) unless the user writes in English. "
    "Use simple, clear, everyday Bangla. Give short answers first, "
    "then details only if asked. For code, explain in Bangla and keep "
    "code and comments in English. If you do not know something, say so "
    "in Bangla instead of guessing."
)

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)


def build_chain():
    # Create the model ONCE and reuse it — rebuilding per message is
    # slow and drops the conversation memory.
    model = ChatOllama(model="qwen2.5:7b", temperature=0.7)
    return PROMPT | model


def summarise(text: str) -> str:
    """One-shot Bangla summary of any text (no memory needed)."""
    model = ChatOllama(model="qwen2.5:7b", temperature=0.3)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Summarise the following text in Bangla, in 2-3 short sentences."),
            ("human", "{text}"),
        ]
    )
    return (prompt | model).invoke({"text": text}).content


def main():
    chain = build_chain()
    history = []
    print("বাংলা চ্যাট — বের হতে 'quit' লিখুন")
    while True:
        user_input = input("আপনি: ").strip()
        if user_input.lower() in {"quit", "exit", "বিদায়"}:
            print("সহকারী: বিদায়! আবার দেখা হবে।")
            break
        if not user_input:
            continue
        answer = chain.invoke({"history": history, "input": user_input})
        print("সহকারী:", answer.content)
        history.append(HumanMessage(content=user_input))
        history.append(AIMessage(content=answer.content))


if __name__ == "__main__":
    main()
