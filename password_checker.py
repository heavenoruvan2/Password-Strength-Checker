import re

def check_password(password):

    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=<>?/]", password):
        score += 1
    else:
        tips.append("Add special characters.")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "score": score,
        "tips": tips
    }
