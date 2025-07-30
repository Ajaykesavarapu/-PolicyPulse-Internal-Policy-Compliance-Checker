import streamlit as st
import requests

st.title("PolicyPulse Compliance Dashboard")

if st.button("Scan Sample Email Inbox"):
    try:
        resp = requests.get("http://localhost:8000/emails/inbox")
        resp.raise_for_status()
        emails = resp.json()
        for email in emails:
            text = email['body']
            scan_resp = requests.post("http://localhost:8000/scan", json={"text": text})
            scan_resp.raise_for_status()
            scan_id = scan_resp.json()["scanId"]
            report = requests.get(f"http://localhost:8000/reports/{scan_id}")
            report.raise_for_status()
            results = report.json().get("results", [])
            st.subheader(f"Email: {email['subject']}")
            if not results:
                st.write("No policy violations found.")
            for flagged in results:
                st.markdown(f"- Line {flagged['line_no']}: **{flagged['text']}** _(Rule: {flagged['rule_id']}, {flagged['description']})_")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")

st.write("---")

st.header("Scan Custom Text")
user_text = st.text_area("Enter text to scan:")
if st.button("Scan Text"):
    if user_text.strip() == "":
        st.warning("Please enter some text to scan.")
    else:
        try:
            scan_resp = requests.post("http://localhost:8000/scan", json={"text": user_text})
            scan_resp.raise_for_status()
            scan_id = scan_resp.json()["scanId"]
            report = requests.get(f"http://localhost:8000/reports/{scan_id}")
            report.raise_for_status()
            results = report.json().get("results", [])
            if not results:
                st.success("No policy violations found.")
            for flagged in results:
                st.markdown(f"- Line {flagged['line_no']}: **{flagged['text']}** _(Rule: {flagged['rule_id']}, {flagged['description']})_")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")
