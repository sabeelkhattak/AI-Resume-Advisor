import json
from app.database import resume_collection, analysis_collection
from app.services.llm_service import analyze_resume_with_ai

def analyze_resume(resume_id: str):
    # 1️⃣ Fetch resume from DB
    resume = resume_collection.find_one({"resume_id": resume_id})

    if not resume or "raw_text" not in resume:
        # Return default analysis if resume missing
        return {
            "score": 0,
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "resume_id": resume_id
        }

    # 2️⃣ Call LLM AI analysis
    ai_response = analyze_resume_with_ai(
        resume_text=resume["raw_text"],
        skills=resume.get("skills", [])
    )

    # 3️⃣ Parse AI JSON response
    try:
        analysis_data = json.loads(ai_response)
    except:
        # If parsing fails, return default
        analysis_data = {}

    # 4️⃣ Ensure all keys exist
    score = analysis_data.get("score", 0)
    strengths = analysis_data.get("strengths", [])
    weaknesses = analysis_data.get("weaknesses", [])
    suggestions = analysis_data.get("suggestions", [])

    # 5️⃣ Add resume_id
    analysis_data_clean = {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions,
        "resume_id": resume_id
    }

    # 6️⃣ Save to DB
    analysis_collection.insert_one(analysis_data_clean)

    return analysis_data_clean
