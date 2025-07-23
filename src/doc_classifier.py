from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def extract_text_from_file(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img)
    elif file_path.lower().endswith(("png", "jpg", "jpeg")):
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
    else:
        print("Unsupported file type:", file_path)
    return text

def detect_doc_type(text):
    text_lower = text.lower()
    if "curriculum vitae" in text_lower or "experience" in text_lower:
        return "Resume"
    elif "passport" in text_lower or "aadhaar" in text_lower:
        return "ID"
    elif "university" in text_lower or "degree" in text_lower:
        return "Education Certificate"
    else:
        return "Unknown"