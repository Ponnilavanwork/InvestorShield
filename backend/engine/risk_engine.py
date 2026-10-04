def calculate_risk(score):
    """
    Convert the internal risk score into a risk level.
    """

    if score >= 75:
        return "VERY HIGH"

    elif score >= 50:
        return "HIGH"

    elif score >= 25:
        return "MODERATE"

    else:
        return "LOW"


def generate_summary(risk_level, indicators):
    """
    Generate a simple explanation based on
    the detected risk indicators.
    """

    if not indicators:
        return (
            "No major risk indicators were detected. "
            "This does not guarantee that the content is safe."
        )

    if risk_level == "VERY HIGH":
        return (
            "Multiple strong risk indicators were detected. "
            "The content requires careful verification before taking any action."
        )

    elif risk_level == "HIGH":
        return (
            "Several risk indicators were detected. "
            "The content should be independently verified before taking action."
        )

    elif risk_level == "MODERATE":
        return (
            "Some risk indicators were detected. "
            "Review the content carefully and verify important claims."
        )

    else:
        return (
            "Few risk indicators were detected. "
            "This analysis does not confirm that the content is safe."
        )


def generate_safe_actions(indicators):
    """
    Generate safety-oriented actions for the user.
    """

    actions = [
        "Do not transfer money until important claims are independently verified.",
        "Do not share OTPs, passwords, PINs, or other sensitive credentials.",
        "Verify the organization or person using an official source.",
        "Be cautious if the message creates urgency or pressure to act immediately."
    ]

    return actions


def build_risk_result(score, indicators):
    """
    Build the complete risk analysis result.
    """

    risk_level = calculate_risk(score)

    summary = generate_summary(
        risk_level,
        indicators
    )

    safe_actions = generate_safe_actions(
        indicators
    )

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "summary": summary,
        "indicators": indicators,
        "safe_actions": safe_actions
    }