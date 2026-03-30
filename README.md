# 🐾 Zoo AI Agent

### 🤖 Multi-Agent AI System powered by Google ADK

> An intelligent zoo assistant that uses multiple AI agents to understand queries, gather knowledge, and deliver structured responses.

---

## 🌟 Features

✨ Multi-Agent Architecture (Greeter → Researcher → Formatter)  
📚 Wikipedia API integration for real-time knowledge  
🧠 Intelligent response generation using Gemini  
☁️ Deployed on Google Cloud Run  
💬 Interactive chat-based UI  

---

## 🧩 Architecture

``` mermaid
graph TD
A[User Input] --> B[Greeter Agent]
B --> C[Research Agent]
C --> D[Wikipedia API / Tools]
D --> E[Formatter Agent]
E --> F[Final Response]

## 🛠️ Tech Stack

| Category        | Technology |
|----------------|------------|
| Language       | Python |
| AI Framework   | Google ADK |
| Model          | Gemini (Vertex AI) |
| Deployment     | Google Cloud Run |
| APIs           | Wikipedia API |
## ⚡ Tech Highlights
- Built using multi-agent architecture
- Integrated real-time knowledge APIs
- Cloud deployed scalable AI system
