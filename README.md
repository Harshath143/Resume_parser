#  Resume Parser using OCR + LLM (Tesseract + Ollama)

This project automates resume parsing by extracting raw text from a PDF and then converting it into structured JSON using a local LLM (like Mistral or LLaMA3 via Ollama). It supports both text-based and scanned PDFs by combining traditional text extraction with OCR fallback.

---

## 🚀 Features

- 📄 Handles both digital and scanned resumes (PDF format).
- 🔍 Uses OCR via Tesseract if direct text extraction fails.
- 🤖 Local LLM integration using [Ollama](https://ollama.com) (no internet API needed).
- 📦 Outputs data in a clean, structured JSON format.

---

## 📁 Project Structure

Resume_parser/|
              |--Resume_parser.py # Main python Script                                                           |---Output.json # Parsed Json Output(auto generated)


---

## 🛠️ Requirements

- Python 3.8 or above
- Tesseract OCR (installed and configured)
- Ollama with supported models (e.g., Mistral or LLaMA3)
- Required Python packages (requirements.txt)

---

## 🧪 Setup Guide

### 1. Clone the Project

```bash
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
```
or Download the Folder Manullly

### 2. Install Python packages

```bash
pip install -r requirements.txt
```
### 3.Install Tesseract OCR

- Windows
- Download from : https://github.com/tesseract-ocr/tesseract
- After installation, make sure the path to tesseract.exe is correct in the script:
```python
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
### 4.Install & Start Ollama

- Download Ollama from : https://ollama.com
- Run the model (e.g., Mistral):
  ```bash
  ollama run mistral
  ```
- This will download and load the model locally. Keep it running during script execution.

  ### 5.Configure the script

  - Open the Reusume_parser and set:
  - The correct path to your resume pdf
  ```python
  PDF_PATH = r"C:\Path\To\Your\Resume.pdf"
  ```
  -The desired model name ("mistral" or "llama3"):
  ```python
  OLLAMA_MODEL = "mistral"
  ```
  ### 6. Run the script
  ```bash
  python Resume_parser.py
  ```
  - If sucessful, youll see the message like:
  ```vbnet
  🎉 Resume parsed! Output saved to output.json
  ```

  ## 📋 Assumptions

- The PDF file is not password-protected or encrypted.
- Tesseract OCR is installed and correctly configured on the system.
- Ollama is installed, and a model like "Mistral" or "LLaMA3" is running locally.
- The resume content is primarily written in English.
- The resume follows a common or standard structure (like most professional resumes).
- The system running the script has internet access during initial model download (only needed once for Ollama).

---

## ⚠️ Limitations

- OCR may not work correctly on low-quality, blurry, or handwritten scanned resumes.
- Unusual resume formats may cause missing or inaccurate fields in the JSON output.
- The script processes only one resume (one PDF file) at a time.
- Performance may be slow when processing very large PDF files.
- No automatic correction for skewed, rotated, or poorly scanned images.
- The local Ollama server must be running while the script is used.
- This script does not perform deep validation (like verifying if an email or phone number is real).

