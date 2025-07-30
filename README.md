PolicyPulse – Internal Policy Compliance Checker
PolicyPulse is a lightweight, open-source compliance tool designed to automatically scan plain text documents and emails for potential internal policy violations. It uses customizable, rule-based scanning (via regular expressions) to flag forbidden terms, Personally Identifiable Information (PII), and other sensitive data commonly restricted in corporate communications.

Key Features
Rule-based scanning engine: Easily configurable policy rules via simple JSON files defining forbidden keywords, email addresses, phone numbers, credit card formats, and other patterns.

API service: FastAPI backend exposing endpoints to scan texts, fetch scan reports, and mock email inbox retrieval.

Interactive Web UI: Streamlit dashboard allows users to trigger scans on sample emails or custom text inputs and review flagged lines inline with descriptive warnings.

Mock email integration: Includes sample inbox data to simulate real-world scanning scenarios.

Testing suite: Unit tests verify scanner accuracy and API response correctness.

Open-source and free: Built entirely on open-source, free-tier Python libraries with no dependency on paid NLP or compliance services.

Why Use PolicyPulse?
Organizations need proactive policy compliance checks to avoid data leaks, inadvertent disclosure of confidential information, and regulatory violations. PolicyPulse provides a simple, extensible tool to integrate compliance scanning into internal workflows and user interfaces—making policy enforcement easier and more transparent.

policypulse/
├── app.py                 # Streamlit web UI
├── api.py                 # FastAPI backend for scan/report endpoints
├── rules.json             # Policy rules file (forbidden terms, PII, etc.)
├── emails_mock.json       # Sample email inbox data
├── scanner.py             # Scanning and rule-matching logic
├── tests/
│   └── test_scanner.py    # Unit tests for rule matching
├── sample_data/
│   └── sample_docs.txt    # Example documents/emails
├── README.md
├── prompt_log.md          # Prompts for ML/rule refining
└── requirements.txt

cd policypulse
. Install dependencies:
pip install -r requirements.txt
# Running the API backend

uvicorn api:app --reload
This starts the API server at `http://localhost:8000`.
## Running the Streamlit UI
In a new terminal window, run:


streamlit run app.py
Open the URL shown in the output (usually `http://localhost:8501`).
Use the buttons to scan the sample inbox or custom text.
## API Endpoints
- POST `/scan` – accepts JSON `{ "text": "some text" }`, returns `{ "scanId": "<id>" }`.
- GET `/reports/{scanId}` – returns JSON results for flagged lines.
- GET `/emails/inbox` – returns mock inbox emails.

## Testing

Run the unit tests with:


python -m unittest discover tests/
## Adding/Updating Rules
Edit `rules.json` with new regex patterns. Each rule must have:
- `id`: unique identifier
- `pattern`: regex pattern to search
- `description`: human-friendly description

## Notes

- No paid APIs or commercial NLP libraries are used.
- Simple regex-based scanning covers common cases; extend with ML if needed.
- `prompt_log.md` is for saving notes related to rules or model prompts.

---

Thank you for using PolicyPulse!








