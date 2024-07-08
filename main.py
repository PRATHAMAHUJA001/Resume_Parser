import re
import json
from PyPDF2 import PdfFileReader
import io


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfFileReader(file)
        text = []
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text.append(page.extract_text())
        return '\n'.join(text)

def extract_information(text):
    info = {}
    
    # Example regex patterns for extracting data
    name_pattern = re.compile(r"Name:\s*(.*)")
    email_pattern = re.compile(r"Email:\s*([\w\.-]+@[\w\.-]+)")
    phone_pattern = re.compile(r"Phone:\s*(\+?\d[\d -]{8,12}\d)")
    education_pattern = re.compile(r"Education:\s*(.*)")
    experience_pattern = re.compile(r"Experience:\s*(.*)")
    
    info['name'] = name_pattern.search(text).group(1).strip() if name_pattern.search(text) else None
    info['email'] = email_pattern.search(text).group(1).strip() if email_pattern.search(text) else None
    info['phone'] = phone_pattern.search(text).group(1).strip() if phone_pattern.search(text) else None
    info['education'] = education_pattern.search(text).group(1).strip() if education_pattern.search(text) else None
    info['experience'] = experience_pattern.search(text).group(1).strip() if experience_pattern.search(text) else None
    
    return info

def parse_resume(file_path):
    if file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    return extract_information(text)

def main():
    file_path = input("Enter the path to the resume file: ")
    resume_data = parse_resume(file_path)
    json_data = json.dumps(resume_data, indent=4)
    print(json_data)
    
    # Save to JSON file
    with open('resume_data.json', 'w') as json_file:
        json_file.write(json_data)
        
if __name__ == "__main__":
    main()
