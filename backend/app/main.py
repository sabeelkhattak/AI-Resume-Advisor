from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import resume
from app.routes import analysis
from fastapi.middleware.cors import CORSMiddleware






app = FastAPI(title="AI Resume Analyzer", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer Backend Running"}
app.include_router(resume.router, prefix="/api")
app.include_router(analysis.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)