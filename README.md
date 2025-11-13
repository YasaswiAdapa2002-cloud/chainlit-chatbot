## Chainlit Gemini Chatbot Template

A simple **AI chatbot** built with [Chainlit](https://docs.chainlit.io/) and [Google Gemini (via LangChain)](https://python.langchain.com/docs/integrations/llms/google_generative_ai/).  
It takes a **topic** as input and lets users ask **multiple questions** about that topic in a conversational flow.

This repository is also designed as a **Backstage software template**, so it can be reused to bootstrap similar AI assistant projects.

## Features

- Interactive chatbot interface powered by **Chainlit**
- Uses **Google Gemini** LLM through `langchain_googlegenai`
- Handles **multi-question sessions** per topic
- Allows user to type `exit` or `quit` to stop chatting
- Includes **Backstage template descriptor** (`catalog-info.yaml`)

---

## Tech Stack

| Component | Description |
|------------|--------------|
| Python | Core language |
|  Chainlit | Chat UI framework |
|  LangChain | LLM orchestration |
|  Gemini | Google Generative AI model |
|  Backstage | Developer portal for software templates |

---

##  How It Works

1. The app asks the user for a **topic** (e.g., "Artificial Intelligence").
2. Once set, users can ask **multiple follow-up questions** related to that topic.
3. The chatbot responds using **Gemini via LangChain**.
4. Typing `exit` or `quit` ends the chat session.
