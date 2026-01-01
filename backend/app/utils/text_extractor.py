import PyPDF2
import docx2txt
from io import BytesIO

def extract_text(filename: str, content: bytes) -> str:
    text = ""

    if filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(BytesIO(content))
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    elif filename.endswith(".docx"):
        text = docx2txt.process(BytesIO(content))

    return text.strip()
