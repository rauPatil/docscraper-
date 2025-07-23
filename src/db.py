import pandas as pd 
import os

DB_FILE = "candidate_data.csv"
REQUIRED_DOCS = ["Resume", "ID", "Education Certificate"]

def load_all_records():
    if os.path.exists(DB_FILE):
       return pd.read_csv(DB_FILE)
    else:
        return pd.DataFrame(columns=["email"] + REQUIRED_DOCS + ["missing"])

def save_record(record):
    df = load_all_records()
    record_row = {
        "email": record["email"],
        "Resume": record["documents"].get("Resume", False),
        "ID": record["documents"].get("ID", False),
        "Education Certificate": record["documents"].get("Education Certificate", False),
        "missing": ", ".join(record["missing"]),
    }
    df = pd.concat([df, pd.DataFrame([record_row])], ignore_index=True)
    df.drop_duplicates(subset="email", keep="last", inplace=True)
    df.to_csv(DB_FILE, index=False)

