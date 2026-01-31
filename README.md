# 🚀 AI Website Summarizer

A production-ready AI-powered web application that extracts structured content from websites and generates intelligent summaries using multiple LLM models via Groq APIs.

---

## 🌟 Features

- URL validation and structured content extraction
- Multi-model LLM selection (Llama 3.1, Llama 3.3, GPT-OSS models)
- Short, detailed, and bullet-point summary modes
- Response time measurement
- Word (.docx) export functionality
- Logging and production-safe backend configuration
- Docker containerization support

---

## 🛠 Tech Stack

- Python 3.11
- Flask
- BeautifulSoup (Web scraping)
- Groq API (LLM inference)
- python-docx (Word export)
- Docker

---

## 🧠 Architecture Overview

1. User submits website URL
2. Backend validates and fetches HTML content
3. Structured extraction removes boilerplate elements
4. Selected LLM model generates summary
5. Summary is exported as a Word document
6. Response time and logs are recorded

---

## 🐳 Run with Docker

Build image:

```bash
docker build -t ai-summarizer .
