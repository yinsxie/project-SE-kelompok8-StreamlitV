import streamlit as st
from gtts import gTTS
from PyPDF2 import PdfReader
import os

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

    # Define state variables for PDF upload and text conversion
    if "pdf_text" not in st.session_state:
        st.session_state["pdf_text"] = ""
    if "pdf_uploaded" not in st.session_state:
        st.session_state["pdf_uploaded"] = False

    # PDF upload functionality
    uploaded_file = st.file_uploader("Upload PDF", type="pdf", key="pdf-upload")
    if uploaded_file is not None:
        st.session_state["pdf_uploaded"] = True
        st.session_state["pdf_text"] = pdf_to_text(uploaded_file)
        st.success(f"Uploaded file: {uploaded_file.name}")
        

    # Button for generating conclusion
    if st.button("Generate Conclusion", key="generate-btn"):
        st.write("Conclusion generation functionality will be implemented here.")
        
    # Display extracted text
    if st.session_state["pdf_text"]:
        st.subheader("Extracted Text")
        st.write(st.session_state["pdf_text"])

    # Button for converting text to speech
    if st.button("Convert to Speech", key="speech-btn"):
        if st.session_state["pdf_uploaded"]:
            output_file = "output.mp3"
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

    
if __name__ == "__main__":
    main()
