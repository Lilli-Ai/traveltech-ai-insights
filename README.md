markdown# ✈️ TravelTech AI Insights Dashboard

> AI-powered intelligence dashboard tracking automation trends in travel tech industry

## 🌐 Live Demo
[TravelTech AI Insights on Hugging Face](https://huggingface.co/spaces/liliaavagyan/TravelTech-AI-Insights)

## 🤖 What it does
An automated pipeline that collects, processes and displays the latest AI & automation news from the travel tech industry — updated in real time.

## ⚙️ Tech Stack & Pipeline
Manual Trigger → SerpApi → Firecrawl → Airtable → HF Space (Gradio)

| Tool | Role |
|------|------|
| **n8n** | Automation pipeline orchestration |
| **SerpApi** | Search & collect travel tech news |
| **Firecrawl** | Scrape & extract article content |
| **Airtable** | Store insights (Title, URL, Summary, Date) |
| **Gradio** | Web dashboard on Hugging Face |
| **Typebot + Groq** | AI chatbot assistant (llama-3.3-70b) |

## 🗂️ Project Structure
- `app.py` — Gradio dashboard reading from Airtable
- `requirements.txt` — Dependencies

## 👩‍💻 Author
**Lilia Avagyan** — AI Automation & Travel Tech  
[LinkedIn](https://linkedin.com/in/lil-ai-travel) | [GitHub](https://github.com/Lilli-Ai)
