# 🤖 AI PDF Chatbot

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-orange)

A simple AI-powered PDF chatbot built using Python, LangChain, FAISS, HuggingFace Embeddings, Groq LLM, and Streamlit.

The application allows users to upload PDF files and ask questions directly from the document using Retrieval-Augmented Generation (RAG).

---
## 🌐 Live Demo

🔗 https://ai-pdf-chatbot-rag-w2tmc2qdjbxlfwktvcmqre.streamlit.app/



## ✨ Features

* Upload PDF files
* Extract text from PDFs
* Convert text into embeddings
* Store embeddings using FAISS
* Ask questions from uploaded PDFs
* Generate AI-based answers
* Simple Streamlit UI

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* Groq API
* PyPDF2

---

## 📂 Project Structure

```bash
pdf_chatbott/
│
├── app.py
├── main.py
├── sample.pdf
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── venv/
```

---

## ⚡ Installation

### Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

### Open Project Folder

```bash
cd ai-pdf-chatbot-rag
```

---

### Create Virtual Environment

```bash
py -3.11 -m venv venv
```

---

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔑 Add API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Project

```bash
python -m streamlit run app.py
```

---

## 🧠 How It Works

1. Upload PDF file
2. Extract text from PDF
3. Split text into chunks
4. Create embeddings using HuggingFace
5. Store embeddings in FAISS
6. Ask questions from the PDF
7. Retrieve relevant chunks
8. Generate final answer using Groq LLM

---

## 🔍 RAG Pipeline

```text
PDF → Text Extraction → Chunking → Embeddings → FAISS → Similarity Search → LLM → Final Answer
```

---

## 🚀 Future Improvements

* Multiple PDF support
* Chat history
* Better UI design
* Voice input
* Deployment on cloud

---

## 👨‍💻 Author

Om Bankar

AI & Data Science Engineering Student
