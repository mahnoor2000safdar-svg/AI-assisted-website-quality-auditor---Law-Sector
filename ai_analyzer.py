import json


# =========================================================
# RULE-BASED SCORE
# =========================================================

def calculate_score(audit):
    score = 0

    if audit.get("contact_info"):
        score += 15

    if audit.get("contact_form"):
        score += 15

    if audit.get("cta"):
        score += 15

    if audit.get("faq"):
        score += 10

    if audit.get("social_links"):
        score += 10

    if audit.get("meta_title"):
        score += 10

    if audit.get("meta_description"):
        score += 10

    if audit.get("mobile_viewport"):
        score += 5

    # Alt-text score
    total_images = audit.get("images_total", 0)
    images_without_alt = audit.get("images_without_alt", 0)

    if total_images == 0:
        score += 10
    else:
        alt_coverage = (
            (total_images - images_without_alt)
            / total_images
        )

        if alt_coverage >= 0.90:
            score += 10
        elif alt_coverage >= 0.70:
            score += 7
        elif alt_coverage >= 0.40:
            score += 4

    return min(score, 100)


# =========================================================
# PRIORITY
# =========================================================

def get_priority(score):
    if score >= 80:
        return "Low"

    elif score >= 60:
        return "Medium"

    else:
        return "High"


# =========================================================
# RULE-BASED RECOMMENDATIONS
# =========================================================

def rule_based_recommendations(audit):

    recommendations = []

    if not audit.get("contact_info"):
        recommendations.append(
            "Add clearly visible phone number, email address, "
            "and office address."
        )

    if not audit.get("contact_form"):
        recommendations.append(
            "Add a contact or consultation request form "
            "to capture potential clients."
        )

    if not audit.get("cta"):
        recommendations.append(
            "Add stronger calls-to-action such as "
            "'Book a Consultation' or 'Contact Us'."
        )

    if not audit.get("faq"):
        recommendations.append(
            "Add an FAQ section covering common legal questions "
            "and client concerns."
        )

    if not audit.get("social_links"):
        recommendations.append(
            "Consider adding professional social media links, "
            "especially LinkedIn."
        )

    if not audit.get("meta_title"):
        recommendations.append(
            "Add a descriptive and SEO-friendly page title."
        )

    if not audit.get("meta_description"):
        recommendations.append(
            "Add a meaningful meta description for search engines."
        )

    if not audit.get("mobile_viewport"):
        recommendations.append(
            "Add a mobile viewport configuration and verify "
            "the website on different screen sizes."
        )

    if audit.get("images_without_alt", 0) > 0:
        recommendations.append(
            f"Add meaningful alt text to "
            f"{audit.get('images_without_alt')} image(s) "
            "for accessibility and SEO."
        )

    if not recommendations:
        recommendations.append(
            "No major rule-based issues were detected. "
            "A human should still review usability, design, "
            "content quality, and legal accuracy."
        )

    return recommendations


# =========================================================
# CREATE MANUAL LLM PROMPT
# =========================================================

def create_ai_prompt(audit):

    facts = {
        "website": audit.get("url"),
        "status": audit.get("status"),
        "contact_info": audit.get("contact_info"),
        "contact_form": audit.get("contact_form"),
        "cta": audit.get("cta"),
        "faq": audit.get("faq"),
        "social_links": audit.get("social_links"),
        "meta_title": audit.get("meta_title"),
        "meta_description": audit.get("meta_description"),
        "mobile_viewport": audit.get("mobile_viewport"),
        "images_total": audit.get("images_total"),
        "images_without_alt": audit.get("images_without_alt"),
        "response_time_seconds": audit.get("response_time_seconds"),
        "page_load_signal": audit.get("page_load_signal")
    }

    prompt = f"""
You are an expert website quality auditor specializing in law-sector
business websites.

Analyze the following automatically detected website facts.

IMPORTANT RULES:
1. Use ONLY the facts provided below.
2. Do not invent features that were not detected.
3. Give a professional judgment suitable for a law firm or legal business.
4. Score the website from 0 to 100.
5. Identify missing features.
6. Give specific and useful recommendations.
7. Assign a priority: Low, Medium, or High.
8. Clearly distinguish facts from your AI judgment.
9. If the website was inaccessible, say that the audit is limited.
10. Return ONLY valid JSON.

AUTOMATICALLY DETECTED FACTS:
{json.dumps(facts, indent=2)}

Return exactly this structure:

{{
    "ai_score": 0,
    "judgment": "Short professional judgment",
    "missing_features": [
        "feature 1",
        "feature 2"
    ],
    "recommendations": [
        "recommendation 1",
        "recommendation 2"
    ],
    "priority": "High"
}}
"""

    return prompt


# =========================================================
# SAVE PROMPT
# =========================================================

def save_ai_prompt(audit, filepath):

    prompt = create_ai_prompt(audit)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(prompt)