import streamlit as st
import requests

# =========================
# CONFIG
# =========================
BACKEND_URL = "http://127.0.0.1:8000"  # Local backend

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-based analysis")

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:
    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):

            # 1️⃣ Upload Resume
            files = {
                "file": (uploaded_file.name, uploaded_file, uploaded_file.type)
            }

            upload_response = requests.post(
                f"{BACKEND_URL}/api/upload-resume",
                files=files
            )

            if upload_response.status_code != 200:
                st.error("Failed to upload resume")
                st.stop()

            resume_id = upload_response.json()["resume_id"]

            # 2️⃣ Analyze Resume
            analysis_response = requests.post(
                f"{BACKEND_URL}/api/analyze-resume/{resume_id}"
            )

            if analysis_response.status_code != 200:
                st.error("Failed to analyze resume")
                st.stop()

            data = analysis_response.json()
            analysis = data.get("analysis", {})  # ✅ always safe

        # =========================
        # DASHBOARD
        # =========================
        st.header("📊 Resume Analysis Dashboard")

        col1, col2 = st.columns(2)

        # 1️⃣ Score Metric
        score = analysis.get("score", 0)
        st.metric("Resume Score", f"{score} / 100")

        # 2️⃣ Progress Bar
        st.progress(score / 100)

        # 3️⃣ Strengths
        st.subheader("✅ Strengths")
        for s in analysis.get("strengths", []):
            st.write(f"- {s}")

        # 4️⃣ Weaknesses
        st.subheader("❌ Weaknesses")
        for w in analysis.get("weaknesses", []):
            st.write(f"- {w}")

        # 5️⃣ Suggestions
        st.subheader("💡 Suggestions")
        for sug in analysis.get("suggestions", []):
            st.write(f"- {sug}")
