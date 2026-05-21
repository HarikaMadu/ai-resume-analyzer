import streamlit as st
import pdfplumber
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Title
st.title("AI Resume Analyzer")

st.markdown(
    "Upload your resume and get AI-powered ATS feedback."
)

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_file is not None:

    resume_text = ""

    # Extract text
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                resume_text += text + "\n"

    # Show extracted text
    # st.subheader("Extracted Resume Text")

    # st.text_area(
    #     "Resume Content",
    #     resume_text,
    #     height=300
    # )

    # Analyze button
    if st.button("Analyze Resume"):

        try:

            prompt = f"""
You are an expert ATS resume reviewer.

Analyze the following resume and provide:

1. Professional Summary
2. Technical Strengths
3. Missing Skills
4. ATS Score out of 100
5. Resume Improvement Suggestions
6. Recommended AIML Projects
7. Career Advice for a 4th year AIML student

Keep the response structured and easy to read.

Resume:
{resume_text}
"""

            with st.spinner("Analyzing Resume..."):

                response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = response.choices[0].message.content

            st.subheader("AI Analysis")

            st.write(result)

        except Exception as e:

            st.error(f"Error: {e}")