from app.utils.text_extractor import extract_text
from app.utils.parser import extract_skills, extract_education, extract_experience
from app.database import resume_collection, analysis_collection


def process_resume(resume_id: str):
    resume = resume_collection.find_one({"resume_id": resume_id})

    if not resume:
        return None

    text = extract_text(resume["filename"], resume["content"])

    parsed_data = {
        "resume_id": resume_id,
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "raw_text": text
    }

    # ✅ Save parsed resume data
    resume_collection.update_one(
        {"resume_id": resume_id},
        {"$set": parsed_data},
        upsert=True
    )

    return parsed_data


def analyze_resume(resume_id: str):
    resume = resume_collection.find_one({"resume_id": resume_id})

    if not resume:
        return None

    analysis_data = {
        "resume_id": resume_id,
        "score": 78,  # TODO: dynamic scoring later
        "strengths": [
            "Strong Python experience",
            "Good project section"
        ],
        "weaknesses": [
            "Lack of quantified achievements"
        ],
        "ats_suggestions": [
            "Add job-specific keywords",
            "Improve formatting consistency"
        ],
        "missing_skills": [
            "Docker",
            "CI/CD"
        ]
    }

    # ✅ VERY IMPORTANT: save analysis in DB
    analysis_collection.update_one(
        {"resume_id": resume_id},
        {"$set": analysis_data},
        upsert=True
    )

    return analysis_data
