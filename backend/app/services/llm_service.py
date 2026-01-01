from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_resume_with_ai(resume_text: str, skills: list):
    prompt = f"""
You are an expert HR and ATS resume evaluator.

Analyze the following resume and give:
1. Resume Score (0–100)
2. Strengths
3. Weaknesses
4. ATS Optimization Suggestions
5. Missing Important Skills

Resume Text:
{resume_text}

Extracted Skills:
{skills}

Respond in JSON format like:
{{
  "score": number,
  "strengths": [],
  "weaknesses": [],
  "ats_suggestions": [],
  "missing_skills": []
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
