import streamlit as st
import pandas as pd
import os
from src.validator import process_all_attachments
from src.inbox_reader import check_inbox
from src.db import load_all_records

st.set_page_config(page_title="📂 Candidate Docs Dashboard", layout="wide")

st.markdown("""
    <style>
        .big-font {font-size: 2.2em !important; font-weight: 700;}
        .stButton>button {width: 100%; font-size: 1.1em;}
        .stTabs [data-baseweb="tab-list"] {justify-content: center;}
        .stDataFrame {background-color: #f9f9f9;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-font">📂 AI Candidate Document Automation</div>', unsafe_allow_html=True)
st.write("Automate candidate document collection, validation, and tracking. Use the controls below to manage automation and review candidate status.")

# Start/Stop Automation
if "running" not in st.session_state:
    st.session_state.running = False

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("▶️ Start Automation", key="start_btn"):
        st.session_state.running = True
        with st.spinner("Running automation..."):
            attachment_senders = {}
            check_inbox(attachment_senders)
            process_all_attachments(attachment_senders)
        st.success("✅ Automation Run Completed!")

with col2:
    if st.button("⏹ Stop Automation", key="stop_btn"):
        st.session_state.running = False
        st.info("Automation stopped.")

st.divider()


df = load_all_records()


tab1, tab2, tab3 = st.tabs([
    "📋 All Candidates",
    "❌ Incomplete Docs",
    "✅ Complete Docs"
])

with tab1:
    st.subheader("All Candidate Records")
    st.dataframe(df, use_container_width=True, height=400)

with tab2:
    st.subheader("Candidates with Missing Documents")
    incomplete = df[df["missing"] != ""]
    st.metric("Count", len(incomplete))
    st.dataframe(incomplete, use_container_width=True, height=400)

with tab3:
    st.subheader("Candidates with Complete Documents")
    complete = df[df["missing"] == ""]
    st.metric("Count", len(complete))
    st.dataframe(complete, use_container_width=True, height=400)


st.markdown(
    "<hr style='margin-top:2em;margin-bottom:1em'>"
    "<center><small>© 2024 Candidate Docs Dashboard</small></center>",
    unsafe_allow_html=True
)