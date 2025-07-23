import os
from collections import defaultdict
from src.doc_classifier import extract_text_from_file, detect_doc_type
from src.email_handler import send_missing_docs_email
from src.db import save_record
from src.file_utils import ATTACHMENT_DIR

REQUIRED_DOCS = ["Resume", "ID", "Education Certificate"]

def validate_documents(detected_docs, candidate_email):
    missing_docs = [doc for doc in REQUIRED_DOCS if doc not in detected_docs]

    candidate_record = {
        "email": candidate_email,
        "documents": {doc: (doc in detected_docs) for doc in REQUIRED_DOCS},
        "missing": missing_docs,
    }

    print(f"\nCandidate: {candidate_record}")
    if missing_docs:
        print(f"Missing: {missing_docs}")
    else:
        print("✅ All required documents received")

    send_missing_docs_email(candidate_email, missing_docs)
    save_record(candidate_record)
    return candidate_record

def process_all_attachments(attachment_senders):
    sender_docs = defaultdict(set)
    for filename in os.listdir(ATTACHMENT_DIR):
        file_path = os.path.join(ATTACHMENT_DIR, filename)
        text = extract_text_from_file(file_path)
        doc_type = detect_doc_type(text)
        print(f"{filename} detected as: {doc_type}")
        if doc_type != "Unknown":
            sender = attachment_senders.get(filename, "unknown@example.com")
            sender_docs[sender].add(doc_type)

    for sender, docs in sender_docs.items():
        validate_documents(docs, candidate_email=sender)
