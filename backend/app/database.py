from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["ai_resume_db"]
resume_collection = db["resumes"]
analysis_collection = db["analysis"]
