# AI Candidate Document Automation

This project helps recruitment teams automatically check if job applicants have sent all required documents via email. It reads unread emails, saves the attachments, detects which documents are submitted using OCR and AI, and sends follow-up emails if anything is missing.

A simple and easy-to-use dashboard (built with Streamlit) lets even non-technical team members view candidate status and control the automation.

---

## Features

- 📥 Automatically reads unread Gmail inbox emails  
- 📎 Downloads attachments and extracts text using OCR  
- 🧠 Detects document types (Resume, ID, Education Certificate, etc.)  
- 📧 Sends up to 3 polite follow-up emails for missing documents  
- 🗂️ Saves candidate info (email, documents received/missing, reminders sent) to CSV or database  
- 🖥️ Streamlit dashboard to view and control everything  

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/docscraper.git
cd docscraper
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root of the project:

```env
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
IMAP_SERVER=imap.gmail.com
```

> ⚠Important: The password should be a Gmail **App Password**, not your regular Gmail password. Instructions are below.

---

## 📹 How to Set Up Gmail App Password

🎥 **https://youtube.com/shorts/WDfvVRVV8Js?si=CgtZfQ4ToNSKwS7o**

### Written Steps:
1. Go to [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Turn on **2-Step Verification** (if not already enabled)
3. Scroll down and click on **App Passwords**
4. Select:  
   - App = **Mail**  
   - Device = **Other** → name it like `DocScraper`  
5. Click **Generate** — you'll get a 16-character password  
6. Paste it in your `.env` file as `EMAIL_PASSWORD`

---

## ▶️ How to Run the App

### Run the backend email processor:

```bash
python -m src.main
```

### Launch the Streamlit web dashboard:

```bash
streamlit run app.py
```

---

## 🧑‍💻 Streamlit Dashboard Tabs

-  **Start/Stop Automation** button  
-  **All Candidates**: Shows all candidate records  
-  **Missing Documents**: Candidates missing documents  
-  **Complete Documents**: Candidates with all required documents  

---

##  Data Storage

- Candidate records are saved in a CSV file by default  
- Can be integrated with **Baserow** or any database of your choice later

---

## 🔮 Future Scope

### 1. AI-Powered Document Classification

We’ll replace our current rule-based detection with an ML model trained using **scikit-learn** or **fastText**. It will better understand Indian documents like:
- Aadhaar Card
- PAN Card
- Offer Letters
- Bank Statements
- Degree Transcripts

### 2. Document AI Integration

We'll integrate **Google Document AI** to:
- Read scanned documents more accurately
- Extract names, dates, university names, etc.
- Handle rotated or noisy documents

### 3. Candidate Upload Portal

A future version may include a secure portal where candidates can directly upload documents through a form instead of emailing them.

---

## 🙌 Built With

- Python 🐍  
- Streamlit 🌐  
- Gmail (IMAP + SMTP) 📬  
- Tesseract OCR 🧠  
- Pandas, schedule, dotenv, and more  

