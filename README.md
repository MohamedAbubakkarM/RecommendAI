# 🛍️ E-commerce Review Analysis Agent

An intelligent AI-powered agentic system that helps users make informed purchasing decisions by analyzing user reviews from the web for any product. 
It combines web scraping, sentiment analysis, and feature summarization to deliver concise product insights, including pros, cons, and a final recommendation.

---

## 🔍 How It Works
This E-commerce Agent follows a **modular agentic architecture** using three specialized agents:

### 1. Fetcher Agent
- Takes the product name as input.
- Searches the web for authentic **user reviews**.
- Collects review data for further analysis.

### 2. Sentiment Analyse Agent
- Analyzes the sentiment behind each review.
- Classifies them into:
  - ✅ Positive  
  - ⚠️ Moderate  
  - ❌ Negative

### 3. Summary Agent
- Extracts **key features**, pros, and cons from user sentiments.
- Compiles a **summary** of user feedback.
- Provides a **final verdict** on whether the product is worth buying or not.

--- 

## 🧠 Tech Stack

- **Python**
- **CrewAI** – Multi-agent orchestration
- **Tavily / Custom Tools** – For review fetching (web scraping/search APIs)
- **Local LLM** – For sentiment classification and summarization
- **Markdown Output** – For clean and structured responses

---

## 📌 Features

- 🧠 Multi-agent collaboration for modular tasks  
- 🕵️ Real-time review gathering  
- 📊 Sentiment-based classification  
- ✍️ Pros and Cons summarization  
- ✅ Buy / Don't Buy recommendation
