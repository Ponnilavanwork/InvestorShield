# InvestorShield

InvestorShield is an AI‑assisted financial scam and misinformation risk analyzer. It accepts a message, URL, or claim and returns an explainable risk score, identified risk indicators, and safe‑action guidance.

## Features
- **Text analysis** – Detects guaranteed returns, regulatory claims, and urgency language.
- **URL analysis** – Flags HTTP, IP hostnames, suspicious keywords, subdomains, long URLs, and unusual characters.
- **Claim extraction** – Pulls out regulatory, return‑guarantee, and urgency claims.
- **Explainable risk scoring** – Converts raw indicators into a risk level (LOW‑VERY HIGH) and a summary.
- **Safe‑action guidance** – Provides user‑friendly steps to verify claims before acting.

## Installation
```bash
pip install -r requirements.txt
```

## Running the API
```bash
uvicorn backend.main:app --reload
```

## API Endpoints
- `GET /` – Health check.
- `POST /analyze` – Accepts JSON with `input_type` (`"url"` or any other string) and `content`.

## Project Structure
```
InvestorShield/
├─ backend/
│  ├─ analyzers/
│  │  ├─ claim_analyzer.py
│  │  ├─ text_analyzer.py
│  │  └─ url_analyzer.py
│  ├─ engine/
│  │  └─ risk_engine.py
│  └─ main.py
├─ requirements.txt
└─ README.md
```

## Future Enhancements
- NLP‑based semantic claim detection.
- Regional‑language support (English/Tamil).
- ML classification for content categories.
- Integration with a front‑end UI.
