import streamlit as st
from PyPDF2 import PdfReader
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from gtts import gTTS

# Convert PDF to text
def pdf_to_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Custom text summarization function
def summarize_text(text, num_sentences=3):
    # Split the text into sentences
    sentences = sent_tokenize(text)

    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    tfidf_matrix = vectorizer.fit_transform(sentences)
    sentence_scores = np.array(tfidf_matrix.sum(axis=1)).ravel()

    top_sentence_indices = sentence_scores.argsort()[-num_sentences:]
    top_sentence_indices.sort()

    # Generate the summary
    summary = ' '.join([sentences[i] for i in top_sentence_indices])
    return summary

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

def show_summarize_page():
    st.title("Text Summarization")

    # Define state variables for PDF upload and text conversion
    if "pdf_text" not in st.session_state:
        st.session_state["pdf_text"] = ""
    if "summary_text" not in st.session_state:
        st.session_state["summary_text"] = ""
    if "pdf_uploaded" not in st.session_state:
        st.session_state["pdf_uploaded"] = False

    # PDF upload functionality
    uploaded_file = st.file_uploader("Upload PDF", type="pdf", key="pdf-upload")
    if uploaded_file is not None:
        st.session_state["pdf_uploaded"] = True
        st.session_state["pdf_text"] = pdf_to_text(uploaded_file)
        st.success(f"Uploaded file: {uploaded_file.name}")
        
        # Automatically generate summary upon PDF upload
        st.session_state["summary_text"] = summarize_text(st.session_state["pdf_text"])

    # Display extracted text
    if st.session_state["pdf_text"]:
        st.subheader("Extracted Text")
        st.write(st.session_state["pdf_text"])
    
    # Button for summarize text
    if st.button("Summarize the paper", key="sum-btn"):
        if st.session_state["summary_text"]:
            st.subheader("Summarized Text")
            st.write(st.session_state["summary_text"])

        else:
            st.warning("Please upload a PDF first")
            

    # Button for converting text to speech
    if st.button("Convert to Speech", key="speech-btn"):
        if st.session_state["pdf_uploaded"]:
            output_file = "summary.mp3"
            text_to_speech(st.session_state["summary_text"], output_file)

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
