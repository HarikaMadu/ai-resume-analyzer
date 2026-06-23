AI Resume Analyzer

An AI-powered Resume Analyzer built using Streamlit, Groq LLM, and PDF processing. This application allows users to upload their resume in PDF format and receive ATS-style feedback, skill analysis, improvement suggestions, and career guidance.

Features

- Upload resume in PDF format
- Extract resume text using PDFPlumber
- AI-powered resume analysis using Groq LLM
- ATS Score generation
- Technical strengths identification
- Missing skills detection
- Resume improvement suggestions
- Recommended AIML projects
- Career guidance for AIML students

Tech Stack

- Python
- Streamlit
- Groq API (Llama 3.1)
- PDFPlumber
- Python Dotenv

Project Workflow

1. User uploads a resume PDF.
2. PDF text is extracted using PDFPlumber.
3. Extracted content is sent to the Groq LLM.
4. AI analyzes the resume.
5. Results are displayed, including:
   - Professional Summary
   - Technical Strengths
   - Missing Skills
   - ATS Score
   - Improvement Suggestions
   - AIML Project Recommendations
   - Career Advice

Installation

Clone the repository:

git clone https://github.com/your-username/ai-resume-analyzer.git

Install dependencies:

pip install -r requirements.txt

Create a ".env" file:

GROQ_API_KEY=your_api_key_here

Run the application:

streamlit run app.py

Future Enhancements

- Job-role specific resume analysis
- Resume keyword optimization
- Resume ranking system
- Multi-format support (PDF, DOCX)
- Downloadable analysis reports

Author

Harika Madu

