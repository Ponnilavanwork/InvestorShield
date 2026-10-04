import re


def analyze_text(text):

    text_lower = text.lower()

    indicators = []
    score = 0

    # ==========================================
    # 1. GUARANTEED RETURN INDICATORS
    # ==========================================

    guaranteed_patterns = [
        r"guaranteed\s+(?:\d+%?\s+)?returns?",
        r"guaranteed\s+(?:\d+%?\s+)?profit",
        r"fixed\s+(?:\d+%?\s+)?returns?",
        r"risk[- ]free\s+(?:returns?|profit)?",
        r"assured\s+(?:returns?|profit)"
    ]

    for pattern in guaranteed_patterns:

        match = re.search(pattern, text_lower)

        if match:

            indicators.append({
                "name": "Guaranteed-return language",
                "severity": "high",
                "evidence": match.group()
            })

            score += 25
            break

    # ==========================================
    # 2. URGENCY / PRESSURE INDICATORS
    # ==========================================

    urgency_patterns = [
    r"join.*?(?:now|today|immediately)",
    r"act.*?(?:now|today|immediately)",
    r"limited\s+time",
    r"today\s+only",
    r"last\s+chance"
]

    for pattern in urgency_patterns:

        match = re.search(pattern, text_lower)

        if match:

            indicators.append({
                "name": "Urgency or pressure language",
                "severity": "medium",
                "evidence": match.group()
            })

            score += 15
            break

    # ==========================================
    # 3. REGULATORY AUTHORITY CLAIMS
    # ==========================================

    authority_patterns = [
        r"sebi\s+approved",
        r"sebi\s+authorized",
        r"official\s+sebi",
        r"government\s+approved",
        r"government\s+authorized"
    ]

    for pattern in authority_patterns:

        match = re.search(pattern, text_lower)

        if match:

            indicators.append({
                "name": "Regulatory authority claim",
                "severity": "high",
                "evidence": match.group()
            })

            score += 20
            break

    # ==========================================
    # FINAL RESULT
    # ==========================================

    return {
        "score": score,
        "indicators": indicators
    }