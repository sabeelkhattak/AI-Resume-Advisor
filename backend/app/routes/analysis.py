from fastapi import APIRouter, HTTPException
from app.services.analysis_service import analyze_resume
from app.database import analysis_collection

router = APIRouter()

@router.post("/analyze-resume/{resume_id}")
def analyze(resume_id: str):
    result = analyze_resume(resume_id)

    if not result:
        raise HTTPException(status_code=404, detail="Resume not found or not parsed")

    return {
        "message": "Resume analyzed successfully",
        "analysis": result
    }


@router.get("/resume-score/{resume_id}")
def get_resume_score(resume_id: str):
    analysis = analysis_collection.find_one(
        {"resume_id": resume_id},
        {"_id": 0, "score": 1}
    )

    if not analysis:
        raise HTTPException(status_code=404, detail="Score not found")

    return analysis
