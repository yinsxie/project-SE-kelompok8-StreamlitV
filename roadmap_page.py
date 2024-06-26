import streamlit as st

def show_roadmap_page():
    
    st.title("🗺️ Roadmap Recommendations")
    st.write("""
    The Roadmap feature provides structured templates and guidelines for various types of academic writing, including thesis, research articles, and other scholarly documents. Users can choose a specific type and receive a detailed roadmap to aid their writing process.
    """)

    # Pilihan jenis penulisan
    option = st.selectbox(
        "Select the type of writing:",
        ["Choose an option", "Thesis", "Scientific Article", "Other Scientific Writing"]
    )

    if option == "Thesis":
        st.header("Thesis Writing Roadmap")

        st.subheader("Tips for Writing a Thesis")
        st.write("""
        - **Start Early**: Begin your research and writing process early to give yourself plenty of time.
        - **Plan Your Structure**: Create an outline to organize your thoughts and structure your thesis.
        - **Stay Focused**: Keep your writing focused on the research problem and objectives.
        - **Seek Feedback**: Regularly seek feedback from your advisor or peers.
        - **Revise and Edit**: Revise your draft multiple times and pay attention to details.
        """)
        
        st.subheader("Introduction")
        st.write("""
        - **Background and Context**: Explain the background of the study and its significance.
        - **Research Problem**: Clearly state the research problem your thesis addresses.
        - **Objectives**: Define the main objectives and goals of your thesis.
        - **Research Questions/Hypotheses**: State the research questions or hypotheses.
        - **Scope and Limitations**: Outline the scope and limitations of your research.
        """)

        st.subheader("Literature Review")
        st.write("""
        - **Overview**: Summarize the key literature relevant to your study.
        - **Identify Gaps**: Identify gaps or limitations in the existing research.
        - **Theoretical Framework**: Explain the theoretical framework guiding your study.
        - **Relevance**: Discuss the relevance of the literature to your research.
        """)

        st.subheader("Methodology")
        st.write("""
        - **Research Design**: Describe your research design and methodological approach.
        - **Data Collection**: Explain the methods and tools used for data collection.
        - **Data Analysis**: Describe the techniques used to analyze the data.
        - **Ethical Considerations**: Mention any ethical considerations.
        """)

        st.subheader("Results")
        st.write("""
        - **Presentation of Data**: Present your data using appropriate visuals.
        - **Key Findings**: Summarize the key findings of your research.
        - **Comparison with Literature**: Compare your findings with the existing literature.
        """)

        st.subheader("Discussion")
        st.write("""
        - **Interpretation**: Interpret the results and discuss their implications.
        - **Limitations**: Acknowledge the limitations of your study.
        - **Recommendations**: Provide recommendations for future research.
        """)

        st.subheader("Conclusion")
        st.write("""
        - **Summary**: Summarize the main findings and contributions of your thesis.
        - **Implications**: Discuss the practical and theoretical implications.
        - **Future Research**: Suggest areas for future research.
        """)

        st.subheader("References")
        st.write("""
        - **Citations**: List all the sources cited in your thesis.
        - **Formatting**: Ensure proper citation style formatting.
        """)

        st.subheader("Appendices")
        st.write("""
        - **Supplementary Material**: Include additional material supporting your thesis.
        - **Data Sets**: Provide data sets or code used in your research, if applicable.
        """)

    elif option == "Scientific Article":
        st.header("Scientific Article Writing Roadmap")
        
        st.subheader("Tips for Writing a Scientific Article")
        st.write("""
        - **Know Your Audience**: Understand the audience and journal you are writing for.
        - **Follow Guidelines**: Adhere to the submission guidelines of your target journal.
        - **Be Clear and Concise**: Write clearly and concisely, avoiding unnecessary jargon.
        - **Highlight Novelty**: Emphasize what is new and significant about your research.
        - **Proofread Thoroughly**: Proofread your manuscript carefully to eliminate errors.
        """)

        st.subheader("Abstract")
        st.write("""
        - **Brief Summary**: Provide a brief summary of the study, including the problem, methods, results, and conclusions.
        - **Keywords**: List relevant keywords.
        """)

        st.subheader("Introduction")
        st.write("""
        - **Background**: Provide background information and context.
        - **Research Problem**: State the research problem.
        - **Objectives**: Define the objectives of the study.
        - **Research Questions/Hypotheses**: State the research questions or hypotheses.
        """)

        st.subheader("Methods")
        st.write("""
        - **Study Design**: Describe the study design and methodological approach.
        - **Data Collection**: Explain data collection methods and tools.
        - **Data Analysis**: Describe data analysis techniques.
        """)

        st.subheader("Results")
        st.write("""
        - **Data Presentation**: Present data using tables, figures, and graphs.
        - **Findings**: Summarize the key findings.
        """)

        st.subheader("Discussion")
        st.write("""
        - **Interpretation**: Interpret the findings and discuss their implications.
        - **Comparison with Literature**: Compare findings with existing literature.
        - **Limitations**: Discuss study limitations.
        - **Future Directions**: Suggest directions for future research.
        """)

        st.subheader("Conclusion")
        st.write("""
        - **Summary**: Summarize the main findings and implications.
        - **Recommendations**: Provide recommendations based on the study findings.
        """)

        st.subheader("References")
        st.write("""
        - **Citations**: Provide a list of references cited in the article.
        - **Formatting**: Ensure proper formatting according to the journal guidelines.
        """)

    elif option == "Other Scientific Writing":
        st.header("Other Scientific Writing Roadmap")

        st.subheader("Tips for Other Scientific Writing")
        st.write("""
        - **Clarify Purpose**: Be clear about the purpose and goals of your writing.
        - **Structure Logically**: Organize your writing in a logical and coherent manner.
        - **Use Clear Language**: Use clear and straightforward language.
        - **Support Arguments**: Back up your arguments with evidence and citations.
        - **Revise and Edit**: Review and refine your work to ensure clarity and accuracy.
        """)
        
        st.subheader("Introduction")
        st.write("""
        - **Context**: Provide context and background.
        - **Problem Statement**: State the problem being addressed.
        - **Objectives**: Define the objectives and goals.
        """)

        st.subheader("Review of Literature")
        st.write("""
        - **Literature Summary**: Summarize relevant literature.
        - **Identify Gaps**: Identify gaps in the literature.
        - **Relevance**: Explain the relevance of the literature to your research.
        """)

        st.subheader("Methodology")
        st.write("""
        - **Approach**: Describe the research approach and design.
        - **Data Collection**: Explain data collection methods.
        - **Data Analysis**: Describe data analysis techniques.
        """)

        st.subheader("Findings")
        st.write("""
        - **Results**: Present the research results.
        - **Interpretation**: Interpret the results.
        """)

        st.subheader("Discussion")
        st.write("""
        - **Implications**: Discuss the implications of the findings.
        - **Limitations**: Acknowledge any limitations.
        - **Future Research**: Suggest areas for future research.
        """)

        st.subheader("Conclusion")
        st.write("""
        - **Summary**: Summarize the key points.
        - **Recommendations**: Provide recommendations.
        """)

        st.subheader("References")
        st.write("""
        - **Citations**: List all cited references.
        - **Formatting**: Ensure proper citation style.
        """)

    else:
        st.write("Please select a writing type to see the roadmap.")

