import streamlit as st
from gtts import gTTS
import PyPDF2
from PyPDF2 import PdfReader
import pyttsx3
import comtypes.client

# Load CSS
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load HTML
def load_html(file_path):
    with open(file_path, "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

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


# Streamlit Application
def main():
    st.set_page_config(page_title="Text to Speech", layout="wide")

    # Load CSS
    load_css("style_fiturTTS.css")

    # Load HTML
    load_html("tts.html")
    
if __name__ == "__main__":
    main()
