from flask import Flask, render_template
import os
import json

from auditor import audit_website
from ai_analyzer import (
    calculate_score,
    get_priority,
    rule_based_recommendations,
    save_ai_prompt
)

from websites import WEBSITES


app = Flask(__name__)


# =========================================================
# MANUAL AI RESULTS
# =========================================================

AI_RESULTS = {

    "RKM Associates": {
        "ai_score": 73,
        "judgment": "The website demonstrates a reasonably professional foundation for a law-sector business, with contact information, a contact form, a CTA, social links, a meta title, and mobile viewport configuration detected. However, the absence of a detected FAQ and meta description, along with limited image alt-text coverage, reduces its overall completeness and accessibility.",
        "missing_features": [
            "FAQ section",
            "Meta description",
            "Alt text for 10 of 13 images"
        ],
        "recommendations": [
            "Add a clear FAQ section addressing common client questions about legal services, consultations, and procedures.",
            "Create a concise, keyword-relevant meta description to improve search-engine presentation and SEO.",
            "Add meaningful descriptive alt text to the 10 images currently missing alt attributes to improve accessibility and image SEO.",
            "Review the website manually on different mobile screen sizes to confirm that the detected mobile viewport translates into a responsive user experience."
        ],
        "priority": "Medium"
    },


    "PK Legal and Associates": {
        "ai_score": 82,
        "judgment": "The website provides a strong professional foundation for a law-sector business. Contact information, CTA, social links, meta title, meta description, and mobile viewport were detected. The main weaknesses are the absence of a detected contact form and FAQ section, while only one of nine images lacks alt text.",
        "missing_features": [
            "Contact or consultation request form",
            "FAQ section",
            "Alt text for 1 of 9 images"
        ],
        "recommendations": [
            "Add a dedicated contact or consultation request form to make it easier for potential clients to submit inquiries.",
            "Add an FAQ section covering common client questions about legal services and consultations.",
            "Add meaningful descriptive alt text to the one image currently missing alt text.",
            "Continue reviewing the website manually across different devices to confirm usability and responsive behavior."
        ],
        "priority": "Medium"
    },


    "Wasif & Fakhar Advocates": {
        "ai_score": 58,
        "judgment": "The website has a basic professional foundation, with contact information, a CTA, meta title, and meta description detected. However, the absence of a contact form, FAQ, social links, and mobile viewport configuration, combined with significant missing alt text, limits its overall business-readiness, accessibility, and mobile usability.",
        "missing_features": [
            "Contact or consultation request form",
            "FAQ section",
            "Social media links",
            "Mobile viewport configuration",
            "Alt text for 6 of 12 images"
        ],
        "recommendations": [
            "Add a dedicated contact or consultation request form to make client inquiries easier.",
            "Add an FAQ section addressing common legal-service and consultation questions.",
            "Add relevant professional social media links, particularly LinkedIn, to improve online presence.",
            "Implement a mobile viewport configuration and manually test the website across different mobile screen sizes.",
            "Add meaningful descriptive alt text to the 6 images currently missing alt attributes."
        ],
        "priority": "High"
    },


    "SR Law": {
        "ai_score": 55,
        "judgment": "The website has a basic professional foundation, with contact information, a CTA, meta title, and mobile viewport detected. However, the absence of a contact form, FAQ, social links, and meta description, together with missing alt text on 15 of 17 images, reduces its overall completeness, accessibility, SEO readiness, and client lead-generation potential.",
        "missing_features": [
            "Contact or consultation request form",
            "FAQ section",
            "Social media links",
            "Meta description",
            "Alt text for 15 of 17 images"
        ],
        "recommendations": [
            "Add a dedicated contact or consultation request form to improve client lead generation.",
            "Add an FAQ section addressing common legal-service and consultation questions.",
            "Add relevant professional social media links to strengthen the firm's online presence.",
            "Create a concise and relevant meta description to improve search-engine visibility.",
            "Add meaningful descriptive alt text to the 15 images currently missing alt attributes for better accessibility and image SEO."
        ],
        "priority": "High"
    },


    "AwaisLaw DRT": {
        "ai_score": 78,
        "judgment": "The website provides a solid professional foundation, with contact information, a contact form, social links, meta title, meta description, and mobile viewport detected. The main weaknesses are the absence of a detected CTA and FAQ section, along with missing alt text on 8 of 12 images. These issues reduce its lead-generation effectiveness, accessibility, and overall completeness.",
        "missing_features": [
            "Clear call-to-action",
            "FAQ section",
            "Alt text for 8 of 12 images"
        ],
        "recommendations": [
            "Add prominent calls-to-action such as 'Book a Consultation' or 'Contact Us' to encourage potential clients to take the next step.",
            "Add an FAQ section covering common legal-service and consultation questions.",
            "Add meaningful descriptive alt text to the 8 images currently missing alt attributes.",
            "Review the website manually on different devices to confirm that its mobile presentation is fully responsive."
        ],
        "priority": "Medium"
    },


    "Junaid, Wasim & Co": {
        "ai_score": 60,
        "judgment": "The website has a basic professional foundation, with contact information, meta title, meta description, mobile viewport, successful page access, and complete alt-text coverage detected. However, no contact form, CTA, FAQ, or social links were detected. These gaps reduce client lead-generation opportunities, user guidance, and overall business-readiness.",
        "missing_features": [
            "Contact or consultation request form",
            "Clear call-to-action",
            "FAQ section",
            "Social media links"
        ],
        "recommendations": [
            "Add a dedicated contact or consultation request form to make it easier for potential clients to submit inquiries.",
            "Add prominent calls-to-action such as 'Book a Consultation' or 'Contact Us' to guide visitors toward taking action.",
            "Add an FAQ section addressing common legal-service and consultation questions.",
            "Add relevant professional social media links to strengthen the firm's online presence and credibility.",
            "Review the website manually for content quality, usability, and client experience."
        ],
        "priority": "Medium"
    }
}


@app.route("/")
def home():

    results = []

    os.makedirs("reports", exist_ok=True)

    for website in WEBSITES:

        audit = audit_website(website["url"])

        rule_score = calculate_score(audit)

        rule_priority = get_priority(rule_score)

        rule_recommendations = rule_based_recommendations(audit)

        ai_result = AI_RESULTS.get(
            website["name"],
            {
                "ai_score": rule_score,
                "judgment": "Manual AI analysis is not available.",
                "missing_features": [],
                "recommendations": [],
                "priority": rule_priority
            }
        )

        # Save AI prompt
        safe_name = (
            website["name"]
            .lower()
            .replace(" ", "_")
            .replace("&", "and")
            .replace(",", "")
        )

        prompt_file = os.path.join(
            "reports",
            f"{safe_name}_ai_prompt.txt"
        )

        save_ai_prompt(audit, prompt_file)

        results.append({
            "name": website["name"],
            "audit": audit,

            # Rule-based results
            "rule_score": rule_score,
            "rule_priority": rule_priority,
            "rule_recommendations": rule_recommendations,

            # AI results
            "ai": ai_result
        })


    # Save structured results
    final_data = []

    for item in results:

        final_data.append({
            "website": item["name"],

            "automatically_detected_facts":
                item["audit"],

            "rule_based_score":
                item["rule_score"],

            "rule_based_priority":
                item["rule_priority"],

            "rule_based_recommendations":
                item["rule_recommendations"],

            "ai_generated_analysis":
                item["ai"]
        })


    with open(
        "reports/final_audit_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            final_data,
            file,
            indent=4,
            ensure_ascii=False
        )


    return render_template(
        "report.html",
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)