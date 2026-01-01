import re

COMMON_SKILLS = [
    "python", "java", "c++", "machine learning", "deep learning",
    "ai", "fastapi", "django", "mongodb", "sql", "docker",
    "git", "linux", "javascript", "react"
]

def extract_skills(text: str):
    text_lower = text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))

def extract_education(text: str):
    education_keywords = ["bachelor", "master", "phd", "bsc", "msc", "bs", "ms"]
    lines = text.lower().split("\n")

    education = []
    for line in lines:
        if any(word in line for word in education_keywords):
            education.append(line.strip())

    return education

def extract_experience(text: str):
    experience_keywords = ["experience", "intern", "worked", "company"]
    lines = text.lower().split("\n")

    experience = []
    for line in lines:
        if any(word in line for word in experience_keywords):
            experience.append(line.strip())

    return experience
