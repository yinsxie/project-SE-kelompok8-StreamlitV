import streamlit as st
from PyPDF2 import PdfReader
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from gtts import gTTS
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BartForConditionalGeneration, BartTokenizer

# Convert PDF to text
def pdf_to_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def calculate_num_sentences(total_sentences, summary_ratio):
    """
    Calculate the number of sentences to extract based on the total number of sentences and the summary ratio.

    :param total_sentences: Total number of sentences in the original text.
    :param summary_ratio: Ratio of sentences to include in the summary.
    :return: Number of sentences to include in the summary.
    """
    return max(1, int(total_sentences * summary_ratio))

def extract_key_sentences(text, summary_ratio):
    # Load SentenceBERT model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences = sent_tokenize(text)
    total_sentences = len(sentences)

    # Calculate the number of sentences to extract
    num_sentences = calculate_num_sentences(total_sentences, summary_ratio)

    embeddings = model.encode(sentences)

    # Compute similarity matrix
    sim_matrix = cosine_similarity(embeddings, embeddings)

    # Rank sentences by their average similarity score
    scores = np.mean(sim_matrix, axis=1)
    ranked_sentences = [sentences[i] for i in np.argsort(scores)[-num_sentences:]]

    return '. '.join(ranked_sentences) + '.'

def summarize_text_with_bart(text, summary_ratio=0.2):
    # Load the pre-trained BART model and tokenizer
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer.batch_encode_plus([text], return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary using the model
    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=4,
        length_penalty=2.0,
        max_length=int(len(text.split()) * summary_ratio),
        min_length=200,  # Ensure minimum length for a paragraph
        no_repeat_ngram_size=3,
        early_stopping=True
    )

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

def show_summarize_page():
    st.title("📚 Text Summarization")
    
    st.write("""
    Welcome to the text summarization tool! Upload a PDF document to get started.
    The tool will extract text from the PDF, summarize it, and provide an option to convert the summary to speech.
    """)

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
        st.session_state["summary_text"] = summarize_text_with_bart(st.session_state["pdf_text"])

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
            