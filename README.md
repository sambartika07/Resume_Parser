# 📄 Resume Parser

## 📌 Overview

The **AI Resume Parser & Applicant Tracking System (ATS)** is a web-based application that automates resume analysis by extracting important candidate information from PDF resumes.

Using **Natural Language Processing (NLP)** and **rule-based extraction techniques**, the system identifies key details such as candidate name, email address, phone number, technical skills, and educational qualifications.

The extracted information is stored in a **PostgreSQL database** and displayed through an ATS dashboard, helping recruiters manage candidate data efficiently.

---

## ✨ Features

✅ Upload resumes in PDF format

✅ Automatic candidate information extraction

✅ Name detection using NLP (spaCy)

✅ Email and phone number extraction

✅ Technical skills identification

✅ Education qualification detection

✅ PostgreSQL database integration

✅ ATS Dashboard for candidate management

✅ Candidate search functionality

✅ Modern and responsive user interface

---

## 🛠️ Technologies Used

### 🔹 Backend

* Python
* Flask

### 🔹 Database

* PostgreSQL

### 🔹 NLP & Parsing

* spaCy
* pdfplumber
* Regular Expressions (Regex)

### 🔹 Frontend

* HTML5
* CSS3
* JavaScript

### 🔹 Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
Resume_Parser/

├── app.py
├── requirements.txt
├── README.md
├── .gitignore

├── uploads/

├── templates/
│   ├── index.html
│   ├── result.html
│   └── admin.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sambartika07/Resume_Parser.git

cd Resume_Parser
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 4️⃣ Configure PostgreSQL

Create a database:

```sql
CREATE DATABASE resume_parser_db;
```

Create the resumes table:

```sql
CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    skills TEXT
);
```

### 5️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## 🔄 Workflow

📄 User uploads a resume

⬇️

📖 PDF text is extracted using pdfplumber

⬇️

🧠 NLP and Regex identify candidate information

⬇️

💾 Data is stored in PostgreSQL

⬇️

📊 Results are displayed on the ATS Dashboard

---

## 📊 Extracted Information

The system extracts:

* 👤 Candidate Name
* 📧 Email Address
* 📱 Phone Number
* 💻 Technical Skills
* 🎓 Educational Qualification

---

## 🚀 Future Enhancements

*  Resume Match Score
*  AI-Based Candidate Ranking
*  Resume Categorization
*  DOCX Resume Support
*  Recruiter Authentication System
*  Advanced Analytics Dashboard
*  Cloud Deployment

---

## 🎓 Learning Outcomes

This project helped me gain practical experience in:

*  Python Programming
*  Flask Web Development
*  PostgreSQL Database Management
*  Natural Language Processing (NLP)
*  Information Extraction Techniques
*  Full-Stack Development
*  Git & GitHub Version Control

---

## 👩‍💻 Author

**Sambartika Jayasingh**

🎓 B.Tech CSE (Artificial Intelligence & Machine Learning)

🏫 Gandhi Engineering College, Bhubaneswar

🔗 GitHub: https://github.com/sambartika07

---

⭐ If you found this project useful, consider giving the repository a star!
