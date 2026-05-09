import streamlit as st

from main import read_pdf
from main import split_text
from main import create_vector_store
from main import ask_question


# =====================================
# Page Settings
# =====================================

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="centered"
)


# =====================================
# Title
# =====================================

st.title("AI PDF Chatbot")

st.write("Upload a PDF and ask questions from it.")


# =====================================
# Upload PDF
# =====================================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)


# =====================================
# If PDF Uploaded
# =====================================

if uploaded_file is not None:

    # Save uploaded PDF temporarily
    with open("temp.pdf", "wb") as file:

        file.write(uploaded_file.getbuffer())


    st.success("PDF Uploaded Successfully")


    # =====================================
    # Read PDF
    # =====================================

    with st.spinner("Reading PDF..."):

        pdf_text = read_pdf("temp.pdf")


    # =====================================
    # Split Text
    # =====================================

    with st.spinner("Splitting Text..."):

        chunks = split_text(pdf_text)


    # =====================================
    # Create Vector Store
    # =====================================

    @st.cache_resource
    def load_vector_store(chunks):

        return create_vector_store(chunks)


    with st.spinner("Creating AI Brain..."):

        vector_store = load_vector_store(chunks)


    # =====================================
    # Ask Question
    # =====================================

    user_question = st.text_input(
        "Ask Question"
    )


    # =====================================
    # Generate Answer
    # =====================================

    if user_question:

        with st.spinner("Thinking..."):

            answer = ask_question(
                vector_store,
                user_question
            )


        st.subheader("Answer")

        st.write(answer)