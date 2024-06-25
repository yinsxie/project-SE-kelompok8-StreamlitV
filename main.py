import streamlit as st

def main():
    st.set_page_config(page_title="Text Summarization and Speech", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Summarize Text", "Text to Speech", "Translate Paper", "Recommendation Paper", "Roadmap to make paper"])

    if page == "Text to Speech":
        import text_to_speech_page
        text_to_speech_page.show_text_to_speech_page()
    elif page == "Summarize Text":
        import summarize_page
        summarize_page.show_summarize_page()
    elif page == "Translate Paper":
        import translate_page
        translate_page.show_translate_page()
    elif page == "Recommendation Paper":
        import recommend_page
        recommend_page.show_recomend_page()
    elif page == "Roadmap to make paper":
        import roadmap_page
        roadmap_page.show_roadmap_page()

if __name__ == "__main__":
    main()
