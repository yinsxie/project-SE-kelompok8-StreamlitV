import streamlit as st
from googletrans import Translator
from PyPDF2 import PdfReader


# Convert PDF to text
def pdf_to_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def translate_text(text, target_language):
    # Inisialisasi objek Translator
    translator = Translator()
    
    # Terjemahkan teks
    translation = translator.translate(text, dest=target_language)
    
    # Kembalikan hasil terjemahan
    return translation.text


def show_translate_page():
    st.title("🌐 Translate Paper")
    st.write("""
    The Translate Paper feature allows users to upload a PDF document and translate its content into another language. This tool is useful for making research accessible to a wider audience by breaking down language barriers.
    """)

    if "pdf_text" not in st.session_state:
        st.session_state["pdf_text"] = ""
    if "translated_text" not in st.session_state:
        st.session_state["translated_text"] = ""
    if "pdf_uploaded" not in st.session_state:
        st.session_state["pdf_uploaded"] = False

    uploaded_file = st.file_uploader("Upload PDF", type="pdf", key="pdf-upload")
    if uploaded_file is not None:
        st.session_state["pdf_uploaded"] = True
        st.session_state["pdf_text"] = pdf_to_text(uploaded_file)
        st.success(f"Uploaded file: {uploaded_file.name}")
    
    # Display extracted text
    if st.session_state["pdf_text"]:
        st.subheader("Extracted Text")
        st.write(st.session_state["pdf_text"])

    languages = {
        "Indonesian": "id",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Simplified Chinese": "zh-cn"
    }

    target_language = st.selectbox("Select target language: ", list(languages.keys()))

    # Tombol untuk mulai terjemahan
    if st.button("Translate"):
        # Terjemahkan teks
        st.session_state["translated_text"] = translate_text(st.session_state["pdf_text"], target_language)
        # Tampilkan hasil terjemahan
        st.write("Translate Results: ")
        st.write(st.session_state["translated_text"])
    