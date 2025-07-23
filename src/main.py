from src.inbox_reader import check_inbox
from src.validator import process_all_attachments

if __name__ == "__main__":
    attachment_senders = {}
    check_inbox(attachment_senders)
    process_all_attachments(attachment_senders)