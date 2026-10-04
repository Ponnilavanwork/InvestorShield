# InvestorShield: Final Project Report & Operating Manual

**Tagline:** "Before you trust it, check it."  
**Target Event:** SANGYAN - Investor Resilience Hackathon  

---

## 1. Executive Summary (For Non-Technical Audiences)
**The Problem:** Retail investors in India (especially first-time users in Tier-2/3 cities) are bombarded with financial content on WhatsApp, Telegram, and YouTube. They often fall victim to scams promising "guaranteed returns," fake regulatory approvals, and manipulative urgency.

**The Solution:** InvestorShield is an AI-assisted pre-action safety layer. It does not give financial advice. Instead, a user simply pastes a suspicious message or URL into the app. The system instantly analyzes the text, detects psychological manipulation (like urgency), verifies regulatory claims, and gives the user an easy-to-understand **Risk Score** along with practical steps to verify the information before they send any money.

---

## 2. Key Features & Accomplishments
* **Message & Claim Analyzer:** Breaks down text to find high-risk language (e.g., "Guaranteed 30% returns").
* **URL Analyzer:** Checks links for suspicious traits (e.g., HTTP instead of HTTPS, IP addresses used as hostnames, excessive subdomains) without actually visiting the dangerous site.
* **Explainable AI:** Doesn't just say "Scam" or "Safe." It breaks down exactly *why* a message is risky (e.g., pointing out the exact sentence that creates false urgency).
* **Bharat-First Accessibility:** The entire User Interface seamlessly toggles between **English** and **Tamil**, making it accessible to regional-language users.
* **Safe-Action Guidance:** Gives the user concrete next steps (e.g., "Do not share OTPs," "Verify using official sources") to pause their momentum and think rationally.

---

## 3. Technical Architecture (For Technical Audiences)
InvestorShield is built on a modern, decoupled client-server architecture:

### Frontend (User Interface)
* **Framework:** React.js powered by Vite for lightning-fast module replacement and building.
* **Styling:** Tailwind CSS (v4) for responsive, utility-first UI design.
* **Icons & UI:** Lucide-React for clean, modern iconography.
* **Networking:** Axios for making asynchronous HTTP POST requests to the backend.

### Backend (Logic & Analysis Engine)
* **Framework:** FastAPI (Python), chosen for its high performance and automatic data validation (via Pydantic).
* **Analyzers:** 
  * `text_analyzer.py`: Uses regex and pattern matching to detect financial return signals and pressure tactics.
  * `claim_analyzer.py`: Extracts specific claims (e.g., "SEBI approved") and assigns them a verification status.
  * `url_analyzer.py`: Safely parses URLs locally to calculate risk based on structure and keywords.
* **Risk Engine:** Aggregates findings into a weighted score out of 100.
* **CORS Middleware:** Configured to allow secure cross-origin requests from the React frontend.

---

## 4. Project Folder Structure
```text
InvestorShield/
│
├── backend/                  # FastAPI Application
│   ├── analyzers/            # Logic for text, claims, and URLs
│   ├── engine/               # Calculates the final Risk Score
│   ├── venv/                 # Python Virtual Environment
│   ├── requirements.txt      # Python dependencies
│   └── main.py               # API Entry Point & CORS setup
│
├── frontend/                 # React Application
│   ├── src/                  # React components (App.jsx, index.css)
│   ├── package.json          # Node.js dependencies
│   └── vite.config.js        # Vite + Tailwind configuration
│
└── FINAL_REPORT.md           # This document
```

---

## 5. Operations Manual (How to Run the Project)
To demonstrate the project to the judges, you need to start both the backend server and the frontend server. 

### Step 1: Start the Backend (FastAPI)
1. Open a terminal (PowerShell or Command Prompt).
2. Navigate to your project folder and into the backend directory:
   ```powershell
   cd path\to\InvestorShield\backend
   ```
3. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\Activate
   ```
4. Start the server:
   ```powershell
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
*(You will see a message saying "Application startup complete". Leave this terminal open.)*

### Step 2: Start the Frontend (React)
1. Open a **second, new terminal**.
2. Navigate to the frontend directory:
   ```powershell
   cd path\to\InvestorShield\frontend
   ```
3. Start the Vite development server:
   ```powershell
   npm run dev
   ```
4. Open your web browser and go to: **http://localhost:5173**

---

## 6. Hackathon Demo Guide (Step-by-Step)
When presenting to the judges, follow this script to show off all features:

1. **Show the UI:** Open `http://localhost:5173`. Point out the clean interface.
2. **Demonstrate Localization:** Click the **"தமிழ்" (Tamil)** button to show how the entire interface translates instantly for Tier-2/3 users. Switch back to **English**.
3. **Run a Test (Message Mode):**
   * Ensure the "Suspicious Message" tab is selected.
   * Paste the following text into the box:
     > *"SEBI approved investment opportunity. Guaranteed 30% returns every month. Join our Telegram group now."*
   * Click **Analyze Risk**.
4. **Explain the Results:**
   * **Risk Score:** Point out the score (e.g., 60/100 - HIGH).
   * **Red Flags:** Show how the AI detected "Guaranteed returns" and "Urgency".
   * **Claims:** Show how the AI extracted "SEBI approved" and marked it as "Needs verification".
   * **Safe Actions:** Show the green box at the bottom prompting the user to pause and verify independently before transferring money.
5. **Run a Test (URL Mode):**
   * Switch to the "Suspicious URL" tab.
   * Enter a fake, risky URL: `http://192.168.1.1/secure/login/bonus`
   * Click **Analyze Risk**.
   * Show how it detects the lack of HTTPS, the use of an IP address instead of a domain name, and the suspicious promotional keywords.
