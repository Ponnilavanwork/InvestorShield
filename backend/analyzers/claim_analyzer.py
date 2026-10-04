import re


def analyze_claims(text):
    """
    Detect important financial claims and pressure
    indicators that may require user verification.
    """

    claims = []

    text_lower = text.lower()

    # =========================================================
    # CLAIM 1: REGULATORY APPROVAL / AUTHORIZATION
    # =========================================================

    regulatory_patterns = [
        r"\bsebi\s+approved\b",
        r"\bsebi\s+authorized\b",
        r"\bsebi\s+registered\b",
        r"\bgovernment\s+approved\b",
        r"\bgovernment\s+authorized\b"
    ]

    for pattern in regulatory_patterns:

        match = re.search(pattern, text_lower)

        if match:
            claims.append({
                "claim": match.group(),
                "category": "Regulatory approval",
                "status": "Needs verification",
                "confidence": "High",
                "explanation": (
                    "The content makes a claim about approval, "
                    "authorization, or registration by a regulatory "
                    "or government authority."
                )
            })

            break

    # =========================================================
    # CLAIM 2: GUARANTEED RETURNS / PROFIT
    # =========================================================

    return_patterns = [
        r"\bguaranteed\s+(?:\d+%?\s+)?returns?\b",
        r"\bguaranteed\s+(?:\d+%?\s+)?profit\b",
        r"\bfixed\s+(?:\d+%?\s+)?returns?\b",
        r"\bassured\s+(?:\d+%?\s+)?returns?\b"
    ]

    for pattern in return_patterns:

        match = re.search(pattern, text_lower)

        if match:
            claims.append({
                "claim": match.group(),
                "category": "Return guarantee",
                "status": "High-risk claim indicator",
                "confidence": "High",
                "explanation": (
                    "The content presents a return or profit "
                    "as guaranteed or assured."
                )
            })

            break

    # =========================================================
    # CLAIM 3: URGENCY / PRESSURE
    # =========================================================

    urgency_patterns = [
        r"\bjoin\b.*?\b(?:now|today|immediately)\b",
        r"\bact\b.*?\b(?:now|today|immediately)\b",
        r"\blimited\s+time\b",
        r"\btoday\s+only\b",
        r"\blast\s+chance\b",
        r"\bdon['’]?t\s+miss\b",
        r"\bdo\s+not\s+miss\b"
    ]

    for pattern in urgency_patterns:

        match = re.search(pattern, text_lower)

        if match:
            claims.append({
                "claim": match.group(),
                "category": "Urgency claim",
                "status": "Pressure indicator",
                "confidence": "Medium",
                "explanation": (
                    "The content uses time pressure that may "
                    "encourage the user to act before verifying "
                    "the information."
                )
            })

            break

    return claims