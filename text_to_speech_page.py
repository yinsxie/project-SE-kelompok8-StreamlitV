import streamlit as st
from gtts import gTTS
from PyPDF2 import PdfReader
import numpy as np

# Convert PDF to text
def pdf_to_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Convert text to speech and save as MP3
def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

def show_text_to_speech_page():
    st.title("🗣️ Text-to-Speech (TTS)")
    st.write("""
    The Text-to-Speech (TTS) feature converts written text into spoken words. This tool is useful for creating audio versions of text documents, enhancing accessibility, and providing a convenient way to listen to content on the go.
    """)

    # if "summary_text" not in st.session_state:
    #     st.session_state["summary_text"] = ""

    if "pdf_text" not in st.session_state:
        st.session_state["pdf_text"] = ""
    if "pdf_uploaded" not in st.session_state:
        st.session_state["pdf_uploaded"] = False
    
    # if st.session_state["summary_text"]:
    #     st.subheader("Summary")
    #     st.write(st.session_state["summary_text"])

    # PDF upload functionality
    uploaded_file = st.file_uploader("Upload PDF", type="pdf", key="pdf-upload")
    if uploaded_file is not None:
        st.session_state["pdf_uploaded"] = True
        st.session_state["pdf_text"] = pdf_to_text(uploaded_file)
        st.success(f"Uploaded file: {uploaded_file.name}")
    
    # Display extracted text
    if st.session_state["pdf_text"]:
        st.subheader("Extracted Text")
        st.write(st.session_state["pdf_text"])

    # Button for converting text to speech
    if st.button("Convert to Speech", key="speech-btn"):
        if st.session_state["pdf_uploaded"]:
            output_file = "audio_paper.mp3"
            text_to_speech(st.session_state["pdf_text"], output_file)

            # Provide audio player and download link
            audio_file = open(output_file, "rb").read()
            st.audio(audio_file, format="audio/mp3")
            st.download_button(
                label="Download MP3",
                data=audio_file,
                file_name=output_file,
                mime="audio/mp3"
            )
        else:
            st.warning("Please upload a PDF file first.")
