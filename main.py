import os

from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_groq import ChatGroq


# =========================================
# Load API Key
# =========================================

import streamlit as st

load_dotenv()

try:

    groq_api_key = st.secrets["GROQ_API_KEY"]

except:

    groq_api_key = os.getenv("GROQ_API_KEY")


# =========================================
# Read PDF
# =========================================

def read_pdf(pdf_file):

    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# =========================================
# Split Text into Chunks
# =========================================

def split_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks


# =========================================
# Create FAISS Vector Store
# =========================================

def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        chunks,
        embeddings
    )

    return vector_store


# =========================================
# Ask Question
# =========================================

def ask_question(vector_store, user_question):

    # Similarity Search
    docs = vector_store.similarity_search(
        user_question,
        k=5
    )

    # Create Context
    context = ""

    for doc in docs:

        context += doc.page_content + "\n"


    # Prompt
    prompt = f"""
    You are an AI PDF assistant.

    Answer the question in a detailed and easy-to-understand way
    using only the provided context.

    Explain properly with enough detail.

    If answer is not available in the context,
    say:
    Answer is not available in the provided PDF.

    Context:
    {context}

    Question:
    {user_question}

    Detailed Answer:
    """


    # Load Groq Model
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )

    # Generate Response
    response = llm.invoke(prompt)

    return response.content


# =========================================
# Main Function
# =========================================

def main():

    print("\n========== AI PDF Chatbot ==========\n")

    # Step 1 - Read PDF
    print("Reading PDF...")

    raw_text = read_pdf("sample.pdf")

    print("PDF Loaded Successfully!")

    # Step 2 - Split Text
    print("\nSplitting Text Into Chunks...")

    chunks = split_text(raw_text)

    print("Total Chunks Created:", len(chunks))

    # Step 3 - Create Vector Store
    print("\nCreating FAISS Vector Store...")

    vector_store = create_vector_store(chunks)

    print("Vector Store Created Successfully!")

    print("\n===== Chatbot Ready =====\n")


    # Chat Loop
    while True:

        user_question = input(
            "Ask Question (type exit to quit): "
        )

        if user_question.lower() == "exit":

            print("\nChatbot Closed.")
            break


        answer = ask_question(
            vector_store,
            user_question
        )

        print("\nAnswer:\n")

        print(answer)

        print()


# =========================================
# Run Program
# =========================================

if __name__ == "__main__":
    main()
