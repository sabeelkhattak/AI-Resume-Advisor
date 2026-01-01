from fastapi import APIRouter, HTTPException
from app.services.career_logic import create_career_plan

router = APIRouter()

@router.post("/career-advice/{resume_id}")
def career_advice(resume_id: str, target_role: str):
    result = create_career_plan(resume_id, target_role)

    if not result:
        raise HTTPException(status_code=404, detail="Career roadmap could not be generated")

    return {
        "message": "Career roadmap generated",
        "roadmap": result
    }
