import re
def extract_target(user_goal):
    PATTERNS = {
    "domain": re.compile(
        r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
    ),
    "ip": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    ),
    "cidr": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)/(?:[0-9]|[12]\d|3[0-2])\b"
    ),
    "range": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\s*-\s*"
        r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    )
    
}
    # Pattern match domain name/IP address/IP range/CIDR notation
    for target_type, pattern in PATTERNS.items():
        match = pattern.search(user_goal)
        if match:
            return {
                "target_type": target_type,
                "value": match[0]
            }
   
    target_type = input("Enter the target type: ")
    value = input("Enter the target: ")
    return {
            "target_type":target_type,
            "value": value
    }
