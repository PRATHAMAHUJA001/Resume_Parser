PDF Resume Parser

This Python project is a resume parser designed to extract key information from PDF resumes and output the data in JSON format. It helps in automating the process of extracting candidate information from resumes, making it easier to manage and analyze large volumes of applications.

Features

PDF Support Only: This parser exclusively supports PDF files, ensuring accurate text extraction from PDF resumes.

Data Extraction: Extracts essential details such as name, email, phone number, education, work experience, skills, and certifications.

JSON Output: Outputs the parsed data in a structured JSON format for easy integration with other systems and applications.

Requirements

Python 3.6+

PyPDF2

re (Regular Expressions)


Installation

Clone the repository:

git clone https://github.com/PRATHAMAHUJA001/Resume_Parser.git

cd pdf-resume-parser

Usage

Place your PDF resume(s) in the resumes directory.

Run the parser script:

python parse_resume.py /path/to/resume.pdf

The parsed data will be printed to the console and saved in a JSON file in the output directory.

Example

Input

Sample resume in PDF format uploaded as Resume.pdf

Output

Output will be a JSON file containing the contents of the PDF File

