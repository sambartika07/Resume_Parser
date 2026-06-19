from flask import Flask, render_template, request
import os
import pdfplumber
import re
import psycopg2
import spacy
import webbrowser

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ---------------- DATABASE CONNECTION ----------------
conn = psycopg2.connect(
    host="localhost",
    port=2347,
    database="resume_parser_db",
    user="postgres",
    password="sam123"
)

cursor = conn.cursor()


# ---------------- HOME PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["resume"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # -------- Extract PDF Text --------
            text = ""
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

            doc = nlp(text)

            # ---------------- NAME (ROBUST LOGIC) ----------------
            name = "Not Found"

            lines = [line.strip() for line in text.split("\n") if line.strip()]

            # Rule-based first (most reliable)
            for line in lines[:5]:
                if (
                    len(line.split()) >= 2
                    and len(line.split()) <= 4
                    and line.replace(" ", "").isalpha()
                    and not any(x in line.lower() for x in ["resume", "skills", "education", "summary"])
                ):
                    name = line
                    break

            # spaCy fallback (safe)
            if name == "Not Found":
                for ent in doc.ents:
                    if ent.label_ == "PERSON":
                        candidate = ent.text
                        if len(candidate.split()) >= 2 and candidate.replace(" ", "").isalpha():
                            name = candidate
                            break

            # ---------------- EMAIL ----------------
            email = re.findall(r"[\w\.-]+@[\w\.-]+", text)

            # ---------------- PHONE ----------------
            phone = re.findall(r"\d{10}", text)

            # ---------------- SKILLS ----------------
            skills_list = [
                "Python", "C", "Java", "SQL",
                "HTML", "CSS", "JavaScript",
                "Full Stack Development"
            ]

            found_skills = [
                skill for skill in skills_list if skill.lower() in text.lower()
            ]

            skills = ", ".join(found_skills)

            # ---------------- EDUCATION ----------------
            education_keywords = ["B.Tech", "BCA", "MCA", "MBA"]

            education = "Not Found"
            for edu in education_keywords:
                if edu.lower() in text.lower():
                    education = edu
                    break

            # ---------------- SAVE TO DB ----------------
            cursor.execute(
                """
                INSERT INTO resumes (name, email, phone, skills)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    name,
                    email[0] if email else "",
                    phone[0] if phone else "",
                    skills
                )
            )

            conn.commit()

            # ---------------- RESULT PAGE ----------------
            return render_template(
                "result.html",
                name=name,
                email=email[0] if email else "Not Found",
                phone=phone[0] if phone else "Not Found",
                skills=skills,
                education=education
            )

    return render_template("index.html")


# ---------------- ADMIN DASHBOARD ----------------
@app.route("/admin")
def admin():
    cursor.execute("SELECT * FROM resumes")
    data = cursor.fetchall()
    return render_template("admin.html", resumes=data)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)