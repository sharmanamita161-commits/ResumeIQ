import streamlit as st
import PyPDF2

st.title("📄 ResumeIQ - AI Resume Analyzer")

st.write("Upload your resume (PDF) to analyze skills and get suggestions.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(text):
    skills = ["python", "java", "c++", "react", "node", "machine learning", "ai"]
    found_skills = []
    
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    score = len(found_skills) * 10

    return found_skills, score

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    skills, score = analyze_resume(text)

    st.subheader("📊 Analysis Result")
    st.write("### Skills Found:")
    st.write(skills)
    st.write("### Resume Score:")
    st.write(score, "/ 100")

    if score < 40:
        st.warning("Add more technical skills to improve your resume.")
    else:
        st.success("Good job! Your resume looks strong.")
