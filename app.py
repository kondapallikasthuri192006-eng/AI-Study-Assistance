import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Study Assistant")
st.write("Ask questions, create notes, summaries and MCQs using GenAI.")

# Get API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

option = st.selectbox(
    "Choose what you want:",
    [
        "Ask a Question",
        "Generate Short Notes",
        "Summarize Text",
        "Generate MCQs",
        "Generate Interview Questions"
    ]
)

topic = st.text_area(
    "Enter your topic or question:",
    placeholder="Example: Explain Machine Learning in simple words"
)

if st.button("Generate 🚀"):

    if not topic.strip():
        st.warning("Please enter a topic or question.")
    else:

        if option == "Ask a Question":
            prompt = f"""
            Answer this question in simple language for a B.Tech student.
            Give a clear explanation with a small example.

            Question:
            {topic}
            """

        elif option == "Generate Short Notes":
            prompt = f"""
            Create short and easy-to-understand study notes on:
            {topic}

            Include:
            - Definition
            - Important points
            - Example
            - Key points for exams
            """

        elif option == "Summarize Text":
            prompt = f"""
            Summarize the following text in simple language.
            Keep the important points and use bullet points.

            Text:
            {topic}
            """

        elif option == "Generate MCQs":
            prompt = f"""
            Create 5 multiple-choice questions about:
            {topic}

            For each question:
            - Give 4 options
            - Clearly mention the correct answer
            - Give a short explanation
            """

        else:
            prompt = f"""
            Generate 10 interview questions about:
            {topic}

            Include beginner and intermediate questions.
            Give a short answer for each question.
            """

        with st.spinner("AI is generating your answer..."):

            response = client.responses.create(
                model="gpt-5-mini",
                input=prompt
            )

        st.subheader("📚 Result")
        st.write(response.output_text)