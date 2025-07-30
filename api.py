from fastapi import FastAPI, Request
from scanner import PolicyScanner
import uuid
import json

app = FastAPI()
scanner = PolicyScanner()
scans = {}

@app.post("/scan")
async def scan_api(req: Request):
    data = await req.json()
    text = data.get('text')
    if text is None:
        return {"error": "Missing 'text' field in request"}
    scan_id = str(uuid.uuid4())
    flagged = scanner.scan_text(text)
    scans[scan_id] = flagged
    return {"scanId": scan_id}

@app.get("/reports/{scan_id}")
def get_report(scan_id: str):
    return {"results": scans.get(scan_id, [])}

@app.get("/emails/{inbox}")
def get_emails(inbox: str):
    with open('emails_mock.json', 'r') as f:
        inbox_data = json.load(f)
    # assuming inbox parameter == "inbox"
    if inbox == "inbox":
        return inbox_data.get("inbox", [])
    else:
        return []
