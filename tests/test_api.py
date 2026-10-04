import sys
import os

# Add backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from main import home, health_check, analyze_content, AnalysisRequest
from analyzers.text_analyzer import analyze_text
from analyzers.claim_analyzer import analyze_claims
from analyzers.url_analyzer import analyze_url
from engine.risk_engine import build_risk_result

def test_home_and_health():
    res1 = home()
    assert res1["version"] == "0.3.0"

    res2 = health_check()
    assert res2["status"] == "healthy"

def test_text_analysis_endpoint():
    req = AnalysisRequest(
        input_type="message",
        content="SEBI approved investment opportunity. Guaranteed 30% returns every month. Join our Telegram group now."
    )
    data = analyze_content(req)
    assert data["risk_score"] == 60
    assert data["risk_level"] == "HIGH"
    assert len(data["indicators"]) == 3
    assert len(data["claims"]) == 3

def test_url_analysis_endpoint():
    req = AnalysisRequest(
        input_type="url",
        content="http://192.168.1.1/secure/login/bonus"
    )
    data = analyze_content(req)
    assert data["risk_score"] > 0
    assert "url_details" in data

def test_url_analyzer_error_safety():
    res1 = analyze_url("invalid_url_without_host")
    assert "url_details" in res1
    assert res1["score"] == 10  # 10 for HTTP scheme

    res2 = analyze_url("")
    assert "url_details" in res2
    assert res2["score"] == 40  # 40 for missing hostname

if __name__ == '__main__':
    test_home_and_health()
    test_text_analysis_endpoint()
    test_url_analysis_endpoint()
    test_url_analyzer_error_safety()
    print("SUCCESS: All backend code and endpoints executed cleanly with 0 errors!")
