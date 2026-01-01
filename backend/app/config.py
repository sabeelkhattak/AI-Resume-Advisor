import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing in .env file")

if not MONGODB_URI:
    raise ValueError("❌ MONGODB_URI is missing in .env file")
