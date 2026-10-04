import re
import ipaddress
from urllib.parse import urlsplit


def analyze_url(url):
    """
    Analyze the structure of a URL for potentially
    suspicious characteristics.

    This analyzer does NOT visit the URL.
    It only examines the URL string locally.
    """

    indicators = []
    score = 0

    # ---------------------------------------------------------
    # CLEAN INPUT
    # ---------------------------------------------------------

    url = url.strip()

    # Add scheme if the user entered something like:
    # example.com/login
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", url):
        url = "http://" + url

    # ---------------------------------------------------------
    # PARSE URL
    # ---------------------------------------------------------

    try:

        parsed = urlsplit(url)

        scheme = parsed.scheme.lower()
        hostname = parsed.hostname
        path = parsed.path.lower()
        query = parsed.query.lower()

    except ValueError:

        return {
            "score": 40,
            "indicators": [
                {
                    "name": "Invalid URL structure",
                    "severity": "medium",
                    "evidence": "Unable to safely parse the URL."
                }
            ],
            "url_details": {
                "scheme": "",
                "hostname": "",
                "path": "",
                "has_query": False
            }
        }

    if not hostname:

        return {
            "score": 40,
            "indicators": [
                {
                    "name": "Missing hostname",
                    "severity": "medium",
                    "evidence": "The URL does not contain a valid hostname."
                }
            ],
            "url_details": {
                "scheme": scheme if 'scheme' in locals() else "",
                "hostname": "",
                "path": "",
                "has_query": False
            }
        }

    hostname = hostname.lower()

    # ---------------------------------------------------------
    # INDICATOR 1: HTTP INSTEAD OF HTTPS
    # ---------------------------------------------------------

    if scheme == "http":

        indicators.append({
            "name": "Unencrypted HTTP connection",
            "severity": "medium",
            "evidence": "URL uses HTTP instead of HTTPS."
        })

        score += 10

    # ---------------------------------------------------------
    # INDICATOR 2: IP ADDRESS INSTEAD OF DOMAIN
    # ---------------------------------------------------------

    try:

        ipaddress.ip_address(hostname)

        is_ip_address = True

        indicators.append({
            "name": "IP address used as hostname",
            "severity": "medium",
            "evidence": hostname
        })

        score += 20

    except ValueError:

        is_ip_address = False

    # ---------------------------------------------------------
    # INDICATOR 3: SUSPICIOUS KEYWORDS
    # ---------------------------------------------------------

    suspicious_keywords = [
        "login",
        "verify",
        "verification",
        "secure",
        "account",
        "update",
        "wallet",
        "bonus",
        "profit",
        "investment",
        "reward",
        "claim",
        "urgent"
    ]

    found_keywords = []

    for keyword in suspicious_keywords:

        if (
            keyword in hostname
            or keyword in path
            or keyword in query
        ):

            found_keywords.append(keyword)

    if found_keywords:

        indicators.append({
            "name": "Sensitive or promotional URL keywords",
            "severity": "medium",
            "evidence": ", ".join(found_keywords)
        })

        score += 10

    # ---------------------------------------------------------
    # INDICATOR 4: EXCESSIVE SUBDOMAINS
    # ---------------------------------------------------------

    # Only check subdomains if the hostname
    # is NOT an IP address.

    if not is_ip_address:

        hostname_parts = hostname.split(".")

        if len(hostname_parts) >= 4:

            indicators.append({
                "name": "Multiple subdomains",
                "severity": "medium",
                "evidence": hostname
            })

            score += 10

    # ---------------------------------------------------------
    # INDICATOR 5: LONG URL
    # ---------------------------------------------------------

    if len(url) > 100:

        indicators.append({
            "name": "Unusually long URL",
            "severity": "low",
            "evidence": f"{len(url)} characters"
        })

        score += 5

    # ---------------------------------------------------------
    # INDICATOR 6: SUSPICIOUS CHARACTERS
    # ---------------------------------------------------------

    suspicious_characters = ["@", "%"]

    found_characters = []

    for character in suspicious_characters:

        if character in url:

            found_characters.append(character)

    if found_characters:

        indicators.append({
            "name": "Unusual URL characters",
            "severity": "medium",
            "evidence": ", ".join(found_characters)
        })

        score += 10

    # ---------------------------------------------------------
    # LIMIT SCORE
    # ---------------------------------------------------------

    score = min(score, 100)

    # ---------------------------------------------------------
    # RETURN RESULT
    # ---------------------------------------------------------

    return {
        "score": score,
        "indicators": indicators,
        "url_details": {
            "scheme": scheme,
            "hostname": hostname,
            "path": parsed.path,
            "has_query": bool(parsed.query)
        }
    }