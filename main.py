import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader
import pyttsx3
import comtypes.client

# Define function to read PDF and convert to speech
def pdf_to_speech(pdf_file):
    
    comtypes.CoInitialize()
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        # page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
    comtypes.CoUninitialize()
    
    return text

# Set up the Streamlit app layout
st.set_page_config(layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
nav_options = ["Translate Languages", "Search Paper", "Publishing"]
nav_choice = st.sidebar.radio("Go to", nav_options)

# Main page title
st.title("Text to Speech Converter")

# File upload section
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
upload_button = st.button("Upload PDF")

# Display sections
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Display Text")
    if uploaded_file is not None and upload_button:
        # Convert PDF to speech and get text
        text = pdf_to_speech(uploaded_file)
        st.write(text)
        st.audio(text, format="audio/mp3")
    else:
        st.write("Text that is read will be displayed here.")

    # Buttons for additional actions
    if st.button("Generate Conclusion"):
        st.write("Conclusion generation is not implemented yet.")
    if st.button("Convert to Speech"):
        if uploaded_file is not None:
            pdf_to_speech(uploaded_file)
            st.success("PDF has been converted to speech.")
        else:
            st.error("Please upload a PDF file first.")

with col2:
    st.write("### Text Explanation")
    st.write("Explanation of the text will be shown here.")