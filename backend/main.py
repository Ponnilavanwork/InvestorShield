from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzers.text_analyzer import analyze_text
from analyzers.claim_analyzer import analyze_claims
from analyzers.url_analyzer import analyze_url
from engine.risk_engine import build_risk_result


app = FastAPI(
    title="InvestorShield API",
    description="Financial scam and misinformation risk analysis API",
    version="0.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    input_type: str
    content: str


@app.get("/")
def home():

    return {
        "message": "InvestorShield API is running",
        "version": "0.3.0"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_content(request: AnalysisRequest):

    # ---------------------------------------------------------
    # URL ANALYSIS
    # ---------------------------------------------------------

    if request.input_type.lower() == "url":

        url_analysis = analyze_url(request.content)

        result = build_risk_result(
            url_analysis["score"],
            url_analysis["indicators"]
        )

        result["url_details"] = url_analysis["url_details"]

        return {
            "input_type": request.input_type,
            **result
        }

    # ---------------------------------------------------------
    # MESSAGE / TEXT ANALYSIS
    # ---------------------------------------------------------

    else:

        # Step 1: Analyze text risk indicators
        analysis = analyze_text(request.content)

        # Step 2: Analyze important claims
        claims = analyze_claims(request.content)

        # Step 3: Build the risk result
        result = build_risk_result(
            analysis["score"],
            analysis["indicators"]
        )

        # Step 4: Add claim analysis
        result["claims"] = claims

        # Step 4.5: Check for explicit URLs in the message
        import re
        url_match = re.search(r'https?://[^\s]+|www\.[^\s]+', request.content)
        if url_match:
            extracted_url = url_match.group(0)
            url_analysis = analyze_url(extracted_url)
            # Combine indicators and increase score based on URL
            result["indicators"].extend(url_analysis["indicators"])
            result["risk_score"] = min(100, result["risk_score"] + url_analysis["score"])
            # Recalculate level and summary
            from engine.risk_engine import calculate_risk, generate_summary
            result["risk_level"] = calculate_risk(result["risk_score"])
            result["summary"] = generate_summary(result["risk_level"], result["indicators"])

        # Step 5: Return the complete result
        return {
            "input_type": request.input_type,
            **result
        }