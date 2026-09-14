import requests
import urllib3
import time
from bs4 import BeautifulSoup

# Disable SSL warning for testing purposes
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def audit_website(url):
    """
    Automatically audits a website and extracts factual signals.
    No AI judgment is performed here.
    """

    result = {
        "url": url,
        "status": "Unknown",
        "error": None,

        # Automatically detected facts
        "contact_info": False,
        "contact_form": False,
        "cta": False,
        "faq": False,
        "social_links": False,
        "meta_title": False,
        "meta_description": False,
        "mobile_viewport": False,
        "images_without_alt": 0,
        "images_total": 0,
        "page_load_signal": False,
        "response_time_seconds": None
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/120 Safari/537.36"
        )
    }

    try:
        start_time = time.perf_counter()

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
            verify=False
        )

        end_time = time.perf_counter()

        response.raise_for_status()

        result["status"] = "Accessible"
        result["page_load_signal"] = True
        result["response_time_seconds"] = round(
            end_time - start_time, 2
        )

        soup = BeautifulSoup(response.text, "html.parser")

        page_text = soup.get_text(" ", strip=True).lower()

        # -------------------------------------------------
        # 1. CONTACT INFORMATION
        # -------------------------------------------------

        contact_keywords = [
            "contact",
            "phone",
            "telephone",
            "email",
            "address",
            "office"
        ]

        result["contact_info"] = any(
            keyword in page_text
            for keyword in contact_keywords
        )

        # -------------------------------------------------
        # 2. CONTACT FORM
        # -------------------------------------------------

        forms = soup.find_all("form")

        result["contact_form"] = len(forms) > 0

        # -------------------------------------------------
        # 3. CTA
        # -------------------------------------------------

        cta_keywords = [
            "contact us",
            "get started",
            "book consultation",
            "schedule consultation",
            "free consultation",
            "request consultation",
            "consultation",
            "call us",
            "learn more"
        ]

        buttons = soup.find_all(["a", "button"])

        button_text = " ".join(
            element.get_text(" ", strip=True).lower()
            for element in buttons
        )

        result["cta"] = any(
            keyword in button_text
            for keyword in cta_keywords
        )

        # -------------------------------------------------
        # 4. FAQ
        # -------------------------------------------------

        result["faq"] = (
            "faq" in page_text
            or "frequently asked questions" in page_text
        )

        # -------------------------------------------------
        # 5. SOCIAL LINKS
        # -------------------------------------------------

        social_domains = [
            "facebook.com",
            "instagram.com",
            "linkedin.com",
            "twitter.com",
            "x.com",
            "youtube.com"
        ]

        social_found = False

        for link in soup.find_all("a", href=True):
            href = link["href"].lower()

            if any(domain in href for domain in social_domains):
                social_found = True
                break

        result["social_links"] = social_found

        # -------------------------------------------------
        # 6. META TITLE
        # -------------------------------------------------

        title = soup.find("title")

        result["meta_title"] = (
            title is not None
            and bool(title.get_text(strip=True))
        )

        # -------------------------------------------------
        # 7. META DESCRIPTION
        # -------------------------------------------------

        meta_description = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        result["meta_description"] = (
            meta_description is not None
            and bool(meta_description.get("content", "").strip())
        )

        # -------------------------------------------------
        # 8. MOBILE VIEWPORT
        # -------------------------------------------------

        viewport = soup.find(
            "meta",
            attrs={"name": "viewport"}
        )

        result["mobile_viewport"] = viewport is not None

        # -------------------------------------------------
        # 9. IMAGE ALT TEXT
        # -------------------------------------------------

        images = soup.find_all("img")

        result["images_total"] = len(images)

        result["images_without_alt"] = sum(
            1
            for img in images
            if not img.get("alt", "").strip()
        )

        return result

    except requests.exceptions.Timeout:
        result["status"] = "Timeout"
        result["error"] = "Website request timed out."
        return result

    except requests.exceptions.ConnectionError:
        result["status"] = "Connection Error"
        result["error"] = "Could not connect to the website."
        return result

    except requests.exceptions.HTTPError as e:
        result["status"] = "HTTP Error"
        result["error"] = str(e)
        return result

    except Exception as e:
        result["status"] = "Error"
        result["error"] = str(e)
        return result