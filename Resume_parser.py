import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
import json
import requests
import os

# ---------- CONFIG ----------
OLLAMA_MODEL = "mistral"  # or "llama3"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # adjust if needed
PDF_PATH = "C:\Projects\AI_Engg_Assessment\.venv\Harshath_Resume.pdf"  # path to the PDF file
# Note: Ensure the PDF file is not password protected or encrypted
OUTPUT_JSON = "output.json"

# Set Tesseract path (only needed on Windows)
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# ---------- STEP 1: Extract text from PDF ----------
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                full_text += extracted
        if full_text.strip():
            print("✅ Extracted text from PDF (no OCR needed).")
            return full_text
    except Exception as e:
        print("⚠️ Text extraction failed, using OCR...")

    # OCR fallback
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    print("✅ Extracted text using OCR.")
    return text

# ---------- STEP 2: Query Ollama for JSON parsing ----------
def extract_resume_data_with_llm(text):
    prompt = f"""
Extract the following fields from this resume text in JSON format (with confidence 0-1 for each):
- name, email, phone, linkedin, skills[], education[{{degree, institution, year}}],
  experience[{{company, title, duration, description}}], certifications[], projects[].
Return null for any missing field.

Text:
{text}
"""
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })

        if response.status_code == 200:
            raw_output = response.json().get("response", "")
            return json.loads(raw_output)
        else:
            print("❌ Ollama returned error:", response.text)
            return {}
    except Exception as e:
        print("❌ Error contacting Ollama:", e)
        return {}

# ---------- STEP 3: Main Logic ----------
def main():
    text = extract_text_from_pdf(PDF_PATH)
    resume_data = extract_resume_data_with_llm(text)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(resume_data, f, indent=4, ensure_ascii=False)

    print(f"🎉 Resume parsed! Output saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
