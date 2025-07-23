import os
from imap_tools import MailBox, AND
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from dotenv import load_dotenv
from collections import defaultdict


load_dotenv()
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")
ATTACHMENT_DIR = "attachments"

REQUIRED_DOCS = ["Resume", "ID", "Education Certificate"]

attachment_senders = {}


def save_attachments(msg, sender):
    os.makedirs(ATTACHMENT_DIR, exist_ok=True)
    for att in msg.attachments:
        filepath = os.path.join(ATTACHMENT_DIR, att.filename)
        # print("File path", filepath)
        with open(filepath, "wb") as f:
            f.write(att.payload)
        # print(f"Saved attachment: {att.filename}")
        attachment_senders[att.filename] = sender
        # print("attachment sender >>> ",attachment_senders)

def check_inbox():
    """Check inbox and download attachments from unread emails."""
    print("Connecting to inbox...")
    with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD) as mailbox:
        # print("mail box object",mailbox)
        for msg in mailbox.fetch(AND(seen=True)):
            print(f"\nFrom: {msg.from_}")
            print(f"Subject: {msg.subject}")
            print(f"Body: {msg.text}")
            save_attachments(msg, sender=msg.from_)
        # print("All unread emails processed.")

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

def process_all_attachments():
    sender_doc = defaultdict(set)
    for filename in os.listdir(ATTACHMENT_DIR):
        file_path = os.path.join(ATTACHMENT_DIR, filename)
        text = extract_text_from_file(file_path)
        doc_type = detect_doc_type(text)
        print(f"{filename} detected as: {doc_type}")
        if doc_type != "Unknown":
            sender = attachment_senders.get(filename, "unknown@example.com")
            print(sender_doc[sender].add(doc_type))
    for sender, docs in sender_doc.items():
        # print("Sender and doc", sender_doc)
        validate_documents(docs, candidate_email=sender)



def validate_documents(detected_docs, candidate_email="unknown@example.com"):
    missing_docs = []
    for doc in REQUIRED_DOCS:
        if doc not in detected_docs:
            missing_docs.append(doc)
    
    candidate_record = {
        "email" : candidate_email,
        "documents" : {doc: (doc in detected_docs) for doc in REQUIRED_DOCS},
        "missing" : missing_docs,
    }
    print(f"\nCandidate: {candidate_record}")
    if missing_docs:
        print(f"Missing documents for {candidate_email}: {missing_docs}")
    else:
        print(f"All required documents received for {candidate_email}")
    return candidate_record






if __name__ == "__main__":
    check_inbox()
    process_all_attachments()
    
