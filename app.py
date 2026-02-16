import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def analyze_resume(text):
    skills = ["python", "java", "machine learning", "data science", "communication"]
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills

if __name__ == "__main__":
    file_path = "sample_resume.pdf"
    resume_text = extract_text_from_pdf(file_path)
    skills = analyze_resume(resume_text)

    print("Detected Skills:")
    for skill in skills:
        print("-", skill)
