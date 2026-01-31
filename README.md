# 🚀 AI Website Summarizer

A production-ready AI-powered web application that extracts structured content from websites and generates intelligent summaries using multiple Large Language Models (LLMs) via Groq APIs.

This project demonstrates backend engineering, structured web scraping, LLM integration, Docker containerization, and production-aware application design.

---

## 🌟 Key Features

- Robust URL validation  
- Structured content extraction (removes boilerplate elements)  
- Multi-model LLM selection:
  - Llama 3.1 8B (Fast)
  - Llama 3.3 70B (Advanced)
  - GPT-OSS 20B
  - GPT-OSS 120B  
- Multiple summary modes:
  - Short
  - Detailed
  - Bullet Points  
- Response time measurement  
- Word (.docx) export with metadata (URL, model used, timestamp)  
- Structured logging system (`app.log`)  
- Production-safe configuration  
- Fully Dockerized  

---

## 🛠 Tech Stack

- Python 3.11
- Flask
- BeautifulSoup4
- Groq API
- python-docx
- Docker

---

## 🧠 System Architecture

User Input (URL)  
↓  
URL Validation  
↓  
HTML Fetching (Requests)  
↓  
Structured Content Extraction (BeautifulSoup)  
↓  
Prompt Engineering  
↓  
LLM Inference (Groq API)  
↓  
Summary + Response Time  
↓  
Word File Export (.docx)  
↓  
Logging & Monitoring  

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

GROQ_API_KEY=your_api_key_here


---

## 🖥 Run Locally

Install dependencies:



pip install -r requirements.txt


Run the application:



python app.py


Open in browser:



http://localhost:5000


---

## 🐳 Run with Docker

Build the Docker image:



docker build -t ai-summarizer .


Run the container:



docker run -p 5000:5000 --env-file .env ai-summarizer


Open in browser:



http://localhost:5000


---

## 📊 Production Considerations

- Request timeout handling  
- Structured logging  
- Environment variable isolation  
- Containerized deployment  
- Safe file handling  
- Model selection flexibility  

---

## 🚀 Future Improvements

- Public deployment (Render / Railway)  
- URL caching system  
- Authentication & usage control  
- Usage analytics dashboard  
- Streaming LLM responses  

---

## 👨‍💻 Author

Rohan Sreeharsha  

