# AI-Assisted Website Quality Auditor – Law Sector

## 1. Project Overview

The **AI-Assisted Website Quality Auditor – Law Sector** is a Python-based web auditing tool designed to evaluate the professionalism, completeness, accessibility, SEO readiness, and business-readiness of law-sector business websites.

The system combines automated website analysis with rule-based scoring and AI-assisted judgment.

The automated auditor retrieves publicly accessible webpages and extracts important website signals using Python, Requests, and BeautifulSoup. These detected facts are then evaluated using predefined rules to calculate a website quality score.

The extracted facts can also be provided to an LLM manually. The LLM analyzes the detected facts and generates a professional judgment, identifies missing features, provides specific recommendations, and assigns a priority level.

A key feature of this project is the clear separation between **automatically detected facts** and **AI-generated judgments and recommendations**.

---

## 2. Project Objectives

The main objectives of this project are:

- To automatically audit law-sector business websites.
- To identify important website quality features.
- To check contact information and contact forms.
- To detect calls-to-action (CTAs).
- To check for FAQ sections.
- To detect social media links.
- To check basic SEO metadata.
- To check mobile viewport configuration.
- To analyze image alt-text coverage.
- To measure a basic HTTP response-time signal.
- To calculate a rule-based website quality score from 0 to 100.
- To use an LLM for professional website judgment.
- To identify missing website features.
- To generate specific and useful recommendations.
- To assign a priority level to website improvements.
- To handle inaccessible, blocked, or slow websites gracefully.
- To generate an easy-to-understand HTML audit report.
- To document limitations and false-positive/false-negative risks.

---

## 3. Key Features

### 3.1 Contact Information Detection

The system checks whether contact-related information is detected on the webpage.

Examples include:

- Phone
- Email
- Address
- Office
- Contact information

The result is recorded as an automatically detected fact.

---

### 3.2 Contact Form Detection

The auditor checks whether an HTML form is present on the webpage.

This provides a basic indication that users may have a form-based communication or lead-generation mechanism.

The system does not assume that the form is fully functional.

---

### 3.3 Call-to-Action Detection

The system checks for recognizable CTA text.

Examples include:

- Contact Us
- Get Started
- Book a Consultation
- Schedule Consultation
- Free Consultation
- Request Consultation
- Call Us
- Learn More

CTA detection is based on the HTML content returned by the website.

---

### 3.4 FAQ Detection

The system checks for recognizable FAQ-related content.

The purpose is to determine whether the website provides an FAQ or similar question-and-answer section.

---

### 3.5 Social Media Link Detection

The auditor checks for links to commonly used social platforms.

Examples include:

- Facebook
- Instagram
- LinkedIn
- X/Twitter
- YouTube

Only links detected in the retrieved HTML are considered.

---

### 3.6 SEO Meta Title

The system checks whether the webpage contains a non-empty HTML title.

A meta title is an important basic SEO element.

---

### 3.7 SEO Meta Description

The system checks whether a meta description is present.

The result is recorded as an automatically detected website fact.

---

### 3.8 Mobile Viewport Detection

The auditor checks whether the webpage contains a mobile viewport configuration.

For example, a website may contain a viewport configuration that allows browsers to adapt the page to different screen sizes.

This is treated as a basic mobile-readiness signal rather than proof of complete mobile responsiveness.

---

### 3.9 Image Alt-Text Analysis

The system counts:

- Total images
- Images without alt text

This provides a basic accessibility and image-SEO signal.

The tool checks whether an alt attribute exists but does not determine whether the alt text is meaningful or accurate.

---

### 3.10 Page Accessibility

The system checks whether the website can be successfully retrieved.

Possible outcomes include:

- Accessible
- Timeout
- Connection Error
- HTTP Error
- Other access-related errors

If a website cannot be accessed, the system reports the limitation instead of stopping the complete audit process.

---

### 3.11 Response Time

The auditor records the approximate HTTP response time for the webpage request.

This is used as a basic performance signal.

It should not be considered a complete website performance or Core Web Vitals measurement.

---

# 4. Technologies Used

The project uses the following technologies:

- Python
- Flask
- Requests
- BeautifulSoup
- HTML
- CSS
- JSON
- Large Language Model (LLM)
- Visual Studio Code

### Python

Python is used for website auditing, data processing, scoring, and application logic.

### Flask

Flask is used to run the web application and display the final audit report.

### Requests

Requests is used to retrieve webpage HTML from publicly accessible websites.

### BeautifulSoup

BeautifulSoup is used to parse HTML and detect website features.

### JSON

JSON is used to represent structured website audit facts.

### LLM

An LLM is used for professional judgment, missing-feature identification, recommendations, and priority assignment.

---

# 5. System Architecture

The system follows the following workflow:

**Law Website → Python Web Auditor → Requests + BeautifulSoup → Automatically Detected Facts → Structured JSON → Rule-Based Scoring + LLM Analysis → HTML Audit Report**

## Main Components

### 5.1 Website Input

The system receives a list of law-sector website URLs from the website configuration file.

### 5.2 Web Auditor

The Python auditor retrieves the webpage using Requests.

BeautifulSoup then parses the returned HTML.

### 5.3 Fact Extraction

The auditor detects:

- Contact information
- Contact forms
- CTAs
- FAQs
- Social links
- Meta title
- Meta description
- Mobile viewport
- Images
- Images without alt text
- Response time
- Page accessibility

### 5.4 Rule-Based Scoring

The detected facts are evaluated using predefined scoring rules.

The result is a score between 0 and 100.

### 5.5 LLM Analysis

The structured website facts are provided to an LLM manually.

The LLM produces:

- AI score
- Professional judgment
- Missing features
- Recommendations
- Priority

### 5.6 Report Generation

Flask uses an HTML template to display the complete audit report.

The report separates automatic findings from AI-generated findings.

---

# 6. Project Structure

The project is organized as follows:

AI-Law-Website-Auditor

    app.py
    auditor.py
    ai_analyzer.py
    websites.py
    requirements.txt
    README.md

    reports/
    
    templates/
        report.html

## File Descriptions

### app.py

This is the main Flask application.

It:

- Runs the web application.
- Loads the selected websites.
- Calls the website auditor.
- Calculates the rule-based score.
- Loads the audit results.
- Generates the final HTML report.

### auditor.py

This file contains the automated website auditing logic.

It uses Requests and BeautifulSoup to extract website facts.

### ai_analyzer.py

This file contains the scoring and analysis logic used by the project.

It includes the rule-based scoring and recommendation logic and supports the structure required for AI-assisted analysis.

### websites.py

This file contains the websites selected for testing.

### report.html

This is the HTML template used to display the final audit report.

### requirements.txt

This file contains the Python packages required by the project.

### reports/

This directory is used for storing generated audit data and AI-related prompt/result files when applicable.

---

# 7. Rule-Based Scoring

The project uses a predefined scoring model with a maximum score of 100.

| Feature | Maximum Score |
|---|---:|
| Contact Information | 15 |
| Contact Form | 15 |
| CTA | 15 |
| FAQ | 10 |
| Social Links | 10 |
| Meta Title | 10 |
| Meta Description | 10 |
| Mobile Viewport | 5 |
| Image Alt Text | 10 |
| **Total** | **100** |

The score is calculated automatically from the detected website facts.

The rule-based score does not depend on the LLM.

---

# 8. Priority Levels

The rule-based system uses the following priority ranges:

| Score Range | Priority |
|---|---|
| 80–100 | Low |
| 60–79 | Medium |
| 0–59 | High |

The priority indicates the level of website improvement suggested by the selected audit rules.

It does not represent the overall quality, reputation, or legal performance of a law firm.

---

# 9. LLM-Assisted Analysis

The project uses an LLM to provide judgment and recommendations based on automatically detected website facts.

The LLM receives structured information such as:

- Website status
- Contact information
- Contact form
- CTA
- FAQ
- Social links
- Meta title
- Meta description
- Mobile viewport
- Image count
- Missing alt text
- Response time

The LLM is instructed to use only the provided facts.

It should not invent features that were not detected.

The expected AI output has the following structure:

```json
{
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
}
```

---

# 10. Manual LLM Workflow

An API key is not required for the manual LLM workflow.

The workflow is:

1. Python audits the website.
2. The auditor extracts factual website signals.
3. The detected facts are represented as structured data.
4. The facts are placed into an AI analysis prompt.
5. The prompt is provided manually to an LLM.
6. The LLM analyzes the supplied facts.
7. The AI result is reviewed by a human.
8. The final result is presented in the audit report.

This approach allows the project to demonstrate LLM-assisted website auditing without requiring a paid API integration.

---

# 11. Fact vs AI Judgment

The project clearly separates objective automated findings from AI-generated interpretation.

## Automatically Detected Facts

These are produced by the Python auditor.

Examples:

- Contact Information: Found
- Contact Form: Found
- CTA: Found
- FAQ: Not Found
- Social Links: Found
- Meta Title: Found
- Meta Description: Not Found
- Mobile Viewport: Detected
- Images Without Alt: 10
- Response Time: 0.93 seconds

These are considered automated observations.

---

## AI-Generated Judgment

The LLM interprets the detected facts and provides:

- AI Score
- Professional Judgment
- Missing Features
- Recommendations
- Priority

The AI is instructed not to claim that a feature exists unless it is present in the supplied facts.

This separation makes the auditing process more transparent.

---

# 12. Websites Tested

The system was tested using six law-sector websites:

1. RKM Associates
2. PK Legal and Associates
3. Wasif & Fakhar Advocates
4. SR Law
5. AwaisLaw DRT
6. Junaid, Wasim & Co

The websites were selected as public webpage test cases.

The project is intended for authorized websites, own websites, or publicly accessible pages where reading the webpage is permitted.

---

# 13. Audit Report

The Flask application generates a professional HTML report.

The report contains the following major sections:

## Audit Overview

Provides a short explanation of the auditing system.

## Automatically Detected Facts

Displays the factual results collected by the Python auditor.

## Rule-Based Findings

Displays the automatic score and rule-based recommendations.

## AI-Generated Judgment & Recommendations

Displays:

- AI Score
- Priority
- AI Judgment
- Missing Features
- AI Recommendations

## Methodology

Explains how the website auditor works.

## Human Double-Check

Explains which findings should be verified manually.

---

# 14. Methodology

The methodology used by the project consists of five main stages.

### Stage 1 – Website Retrieval

Requests retrieves the publicly accessible webpage.

### Stage 2 – HTML Analysis

BeautifulSoup parses the webpage HTML.

### Stage 3 – Fact Extraction

The system detects the predefined website features.

### Stage 4 – Scoring and AI Analysis

The detected facts are evaluated using the rule-based scoring system and can also be analyzed by an LLM.

### Stage 5 – Report Generation

Flask presents the results in a structured HTML report.

---

# 15. Error Handling

The system is designed to continue working when an individual website cannot be accessed.

It handles common problems including:

- Request timeout
- Connection errors
- HTTP errors
- SSL certificate problems
- Unexpected errors

For example, if one website times out, the auditor records the website as inaccessible or limited and continues processing the remaining websites.

This prevents one problematic website from stopping the complete audit.

---

# 16. Inaccessible Website Handling

If a website is inaccessible, the report clearly indicates that the audit is limited.

For example:

**Status: Timeout**

The report may also display an audit limitation message explaining that the website could not be fully analyzed.

No unsupported website features should be assumed when a website cannot be accessed.

---

# 17. Ethical and Authorized Usage

This project is intended for responsible website auditing.

The auditor should only be used on:

- Websites owned by the user
- Authorized test websites
- Publicly accessible websites where reading the webpage is permitted

The tool should not be used to:

- Bypass authentication
- Bypass security controls
- Access private information
- Scan restricted systems
- Attempt unauthorized security testing

The project focuses on analyzing publicly available webpage content.

---

# 18. Limitations

The tool provides useful automated signals, but it does not perform a complete professional website audit.

## 18.1 JavaScript-Heavy Websites

The auditor mainly analyzes the HTML returned by the server.

Websites that generate content dynamically using JavaScript may have features that are not detected.

---

## 18.2 Mobile Responsiveness

The current mobile check detects the presence of a mobile viewport configuration.

This does not prove that every part of the website is fully responsive.

Actual mobile responsiveness should be manually tested on different devices and screen sizes.

---

## 18.3 Contact Information Detection

Contact information detection uses predefined keywords and page content.

This can produce false positives.

For example, a webpage may contain the word "contact" without providing complete contact information.

---

## 18.4 Contact Form Detection

The system checks whether an HTML form is present.

It does not verify whether the form:

- Works correctly
- Sends messages successfully
- Is connected to email
- Is secure
- Is specifically designed for lead generation

---

## 18.5 CTA Detection

CTA detection depends on recognizable button or link text.

Icon-only CTAs or dynamically generated CTAs may not be detected.

---

## 18.6 FAQ Detection

FAQ detection depends on recognizable FAQ-related content.

A website may provide useful questions and answers without using the word "FAQ".

---

## 18.7 Social Link Detection

Social links are detected from the HTML returned by the website.

Links generated dynamically through JavaScript may not be detected.

---

## 18.8 Image Alt Text

The system checks whether an alt attribute exists.

It does not evaluate whether the alt text is meaningful, accurate, or useful for accessibility.

---

## 18.9 Response Time

The response time is a basic HTTP request measurement.

It is not a complete website performance measurement.

It does not represent:

- Full page rendering time
- JavaScript execution time
- Image loading time
- Core Web Vitals
- Real user network conditions

---

## 18.10 AI Limitations

AI-generated recommendations are judgment-based.

The LLM may misunderstand the importance of a particular feature or provide a recommendation that requires additional human verification.

Therefore, AI output should be treated as assistance rather than absolute truth.

---

# 19. False Positives and False Negatives

The automated auditor uses HTML-based and keyword-based detection.

Therefore, false positives and false negatives are possible.

## False Positive

A feature may be reported as present even though it does not provide the expected functionality.

For example, the word "contact" may appear on a webpage, but a useful contact mechanism may not actually be available.

## False Negative

A feature may exist but not be detected.

For example, a CTA generated dynamically using JavaScript may not appear in the HTML retrieved by Requests.

Human verification is therefore important.

---

# 20. Human Double-Check

Automated detection and AI judgment should be reviewed by a human before final conclusions are made.

The following areas should be manually checked:

- Visual professionalism
- Website layout
- Actual mobile responsiveness
- Navigation usability
- Content quality
- Legal information accuracy
- Contact form functionality
- CTA usefulness
- Client experience
- Accuracy of AI recommendations

The final evaluation should not rely only on the automated score.

---

# 21. Installation

Make sure Python is installed on the computer.

Check the Python version using:

```bash
python --version
```

Install the project dependencies using:

```bash
python -m pip install -r requirements.txt
```

---

# 22. Running the Application

Open the VS Code terminal inside the project folder.

Run:

```bash
python app.py
```

The Flask application should start on a local address similar to:

```text
http://127.0.0.1:5000
```

Open this address in a web browser.

The website audit report will then be displayed.

---

# 23. Requirements

The project requires the following Python packages:

- Flask
- Requests
- BeautifulSoup4
- urllib3

If an LLM API integration is added in the future, the required LLM SDK can also be installed.

The current manual LLM workflow does not require an API key.

---

# 24. Output

The main output of the system is an HTML audit report.

The report contains:

- Website name
- Website URL
- Website status
- Automatically detected facts
- Rule-based score
- Rule-based findings
- AI score
- AI judgment
- Missing features
- AI recommendations
- Priority
- Methodology
- Limitations
- Human double-check guidance

Structured JSON files may also be stored in the reports directory when generated by the application.

---

# 25. Example Audit Data

An example of automatically detected website facts is:

```json
{
    "website": "https://rkmassociates.com/",
    "status": "Accessible",
    "contact_info": true,
    "contact_form": true,
    "cta": true,
    "faq": false,
    "social_links": true,
    "meta_title": true,
    "meta_description": false,
    "mobile_viewport": true,
    "images_total": 13,
    "images_without_alt": 10,
    "response_time_seconds": 0.93,
    "page_load_signal": true
}
```

These values represent automatically detected facts.

The AI does not directly modify these facts.

---

# 26. Example AI Analysis Structure

After receiving the detected facts, the LLM produces a structured result such as:

```json
{
    "ai_score": 73,
    "judgment": "The website demonstrates a reasonably complete foundation for a professional legal business website, with strong contact accessibility and basic SEO and mobile indicators. However, the absence of an FAQ and meta description, together with incomplete image alt-text coverage, reduces overall website quality.",
    "missing_features": [
        "FAQ section",
        "Meta description"
    ],
    "recommendations": [
        "Add a concise FAQ section addressing common client questions.",
        "Create a relevant meta description for improved search visibility.",
        "Review images without alt text and add meaningful descriptions where appropriate."
    ],
    "priority": "Medium"
}
```

The exact AI output depends on the detected facts and the LLM response.

---

# 27. Advantages of the System

The project provides several advantages:

- Automated website auditing
- Fast analysis
- Consistent rule-based scoring
- Structured website facts
- AI-assisted professional judgment
- Specific recommendations
- Clear fact-versus-judgment separation
- Graceful error handling
- Easy-to-read HTML report
- Support for multiple websites
- Simple and extendable Python architecture
- Documented limitations

---

# 28. Why AI is Used

A rule-based system can determine whether a feature exists, but it has limited ability to provide contextual recommendations.

For example:

**Automatically detected fact:**

FAQ = Not Found

This is an objective detection.

The LLM can then interpret the finding and provide a professional recommendation about why an FAQ may be useful for a legal business website.

Therefore, the project combines:

**Automated Detection + Rule-Based Scoring + AI-Assisted Judgment**

This combination provides both measurable website signals and human-readable recommendations.

---

# 29. Security Considerations

The auditor should not be used to access private or restricted information.

The application is intended for public webpage analysis.

The current local testing implementation may use relaxed SSL verification for websites with certificate configuration problems. This is only a testing workaround and should not be considered a secure production configuration.

For production deployment, proper SSL certificate verification should be enabled.

The application should also avoid storing sensitive information.

---

# 30. Future Improvements

The project can be improved in several ways.

## Browser-Based Auditing

Playwright could be integrated to analyze JavaScript-heavy websites and dynamically generated content.

This could improve:

- Dynamic content detection
- Mobile viewport testing
- Browser-based rendering
- More realistic performance measurements

---

## Advanced SEO Analysis

Future versions could check:

- Heading hierarchy
- Canonical tags
- Robots meta tags
- Open Graph tags
- Structured data
- Sitemap availability

---

## Advanced Accessibility Analysis

Future versions could check:

- ARIA attributes
- Form labels
- Keyboard navigation
- Color contrast
- Heading structure
- Accessibility errors

---

## Advanced Performance Analysis

Future versions could include:

- Full page load timing
- Resource timing
- Core Web Vitals
- JavaScript performance
- Page-size analysis

---

## Dashboard

A future version could provide:

- Website comparison charts
- Website ranking
- Feature comparison
- Historical audit results
- Score trends
- PDF export

---

## Automated LLM API Integration

A future production version could integrate an LLM API securely using environment variables.

An API key should never be placed directly inside source code or uploaded to GitHub.

---

# 31. Academic Assignment Requirements Covered

The project addresses the major requirements of the website auditing assignment.

| Requirement | Implementation |
|---|---|
| 5–8 law websites | 6 websites tested |
| Website fact extraction | Requests + BeautifulSoup |
| Contact information | Automated detection |
| Contact forms | Automated detection |
| CTA | Automated detection |
| FAQ | Automated detection |
| Social links | Automated detection |
| SEO metadata | Meta title and description checks |
| Mobile readiness | Viewport detection |
| Image accessibility | Alt-text coverage |
| Response-time signal | HTTP response time |
| Rule-based scoring | 0–100 scoring system |
| LLM analysis | Manual LLM workflow |
| Missing features | AI-generated |
| Recommendations | AI-generated |
| Priority | Rule-based / AI analysis |
| Fact vs AI separation | Separate report sections |
| Error handling | Timeout/connection/HTTP handling |
| HTML report | Flask + HTML/CSS |
| Limitations | Documented |
| Human double-check | Documented |

---

# 32. Project Outcome

The completed project demonstrates how automated website auditing and AI-assisted reasoning can be combined to evaluate law-sector business websites.

The Python auditor collects objective website signals.

The rule-based engine converts these signals into a measurable score.

The LLM interprets the supplied facts and provides professional recommendations.

The HTML report presents the information in a structured and user-friendly format.

The project therefore demonstrates the integration of:

**Web Auditing**

**Web Scraping**

**Rule-Based Logic**

**Structured JSON Data**

**LLM-Assisted Reasoning**

**HTML Report Generation**

---

# 33. Conclusion

The **AI-Assisted Website Quality Auditor – Law Sector** provides a practical framework for evaluating important aspects of law-sector business websites.

The system automatically detects website features such as contact information, forms, CTAs, FAQs, social links, SEO metadata, mobile viewport configuration, image alt-text coverage, accessibility, and response time.

The detected facts are evaluated using a rule-based scoring system and can also be analyzed by an LLM for professional judgment and recommendations.

A major strength of the project is the separation between automatically detected facts and AI-generated judgments. This improves transparency and makes it easier for a human reviewer to verify the results.

The project also documents its limitations, false-positive and false-negative risks, and the need for human verification.

Overall, the system demonstrates how traditional rule-based website auditing can be enhanced with AI-assisted analysis to produce more informative and actionable website quality reports.

---

# 34. Academic Project Information

**Project Title:** AI-Assisted Website Quality Auditor – Law Sector

**Project Type:** Academic / Week 4 Assignment

**Domain:** Web Development, Website Auditing, Artificial Intelligence

**Technologies:** Python, Flask, Requests, BeautifulSoup, HTML, CSS, JSON, LLM

**Primary Purpose:** Automated website quality auditing and AI-assisted recommendations

**Target Sector:** Law and Legal Businesses