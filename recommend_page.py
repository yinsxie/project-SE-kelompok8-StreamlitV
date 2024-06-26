import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

# Contoh dataset paper
data = {
    "title": [
        "Deep Learning for Natural Language Processing",
        "Machine Learning in Healthcare",
        "Applications of AI in Finance",
        "Neural Networks for Image Recognition",
        "AI and Ethics",
        "Data Science in Education",
        "Quantum Computing for Beginners",
        "The Future of Robotics",
        "AI in Autonomous Vehicles",
        "Big Data Analytics"
    ],
    "abstract": [
        "This paper discusses the advancements in deep learning techniques for natural language processing applications.",
        "An overview of machine learning applications in healthcare, including predictive analytics and personalized medicine.",
        "Examining the impact of artificial intelligence in the financial sector, including trading algorithms and risk management.",
        "An in-depth look at the use of neural networks for image recognition and classification.",
        "Exploring the ethical considerations and implications of artificial intelligence development.",
        "The role of data science in improving educational outcomes and personalized learning.",
        "An introductory guide to quantum computing and its potential applications.",
        "Discussing the current state and future prospects of robotics technology.",
        "Advancements in AI for developing autonomous vehicles and their societal impact.",
        "Utilizing big data analytics to drive business insights and innovation."
    ]
}

# Mengonversi dataset ke DataFrame
df = pd.DataFrame(data)

def recommend_papers(topic, df):
    # Menggabungkan judul dan abstrak untuk analisis TF-IDF
    df['content'] = df['title'] + " " + df['abstract']
    
    # Vectorizing content using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    
    # Vectorizing input topic
    topic_tfidf = tfidf.transform([topic])
    
    # Calculating cosine similarity
    cosine_similarities = linear_kernel(topic_tfidf, tfidf_matrix).flatten()
    
    # Getting top 5 recommendations
    related_docs_indices = cosine_similarities.argsort()[:-6:-1]
    
    # Returning titles of the recommended papers
    recommendations = df['title'].iloc[related_docs_indices]
    return recommendations

def show_recommend_page():
    
    st.title("📄 Recommend Paper")
    st.write("""
    The Recommend Paper feature suggests relevant academic papers based on a user's input topic. It leverages natural language processing techniques to find papers with similar topics, helping users discover related research and literature.
    """)
    
    # Input topik dari user
    topic = st.text_input("Enter the topic of the paper you want to write:")
    
    if topic:
        recommendations = recommend_papers(topic, df)
        st.subheader("Recommended Papers")
        for idx, title in enumerate(recommendations):
            st.write(f"{idx+1}. {title}")

