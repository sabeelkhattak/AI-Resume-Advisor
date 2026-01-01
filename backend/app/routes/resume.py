from fastapi import APIRouter, UploadFile, File, HTTPException
import uuid
from app.database import resume_collection
from app.services.resume_service import process_resume, analyze_resume

router = APIRouter(
    tags=["Resume"]  # ⭐ Swagger grouping
)

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    resume_id = str(uuid.uuid4())

    resume_collection.insert_one({
        "resume_id": resume_id,
        "filename": file.filename,
        "content": content
    })

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume_id
    }

@router.post("/parse-resume/{resume_id}")
def parse_resume(resume_id: str):
    parsed = process_resume(resume_id)
    if not parsed:
        raise HTTPException(status_code=404, detail="Resume not found")

    return {
        "message": "Resume parsed successfully",
        "data": parsed
    }

@router.post("/analyze-resume/{resume_id}")
def analyze_resume_endpoint(resume_id: str):
    analysis = analyze_resume(resume_id)

    # ✅ Fix: If analysis fails, return default structure
    if not analysis:
        analysis = {
            "score": 0,
            "strengths": [],
            "weaknesses": [],
            "suggestions": [],
            "resume_id": resume_id
        }

    return {
        "message": "Resume analyzed successfully",
        "analysis": analysis
    }
