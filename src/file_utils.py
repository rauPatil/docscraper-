import os

ATTACHMENT_DIR = "attachments"

def save_attachments(msg, sender, attachment_senders):
    os.makedirs(ATTACHMENT_DIR, exist_ok=True)
    for att in msg.attachments:
        filepath = os.path.join(ATTACHMENT_DIR, att.filename)
        with open(filepath, "wb") as f:
            f.write(att.payload)
        attachment_senders[att.filename] = sender