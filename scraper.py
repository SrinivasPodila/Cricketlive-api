import requests
from bs4 import BeautifulSoup

def get_live_scores():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Each match is inside a div with class "cb-mtch-lst"
        matches = soup.find_all("div", class_="cb-mtch-lst")

        results = []
        for match in matches:
            # Match title is inside an <a> tag with class 'text-hvr-underline'
            title_tag = match.find("a", class_="text-hvr-underline")
            title = title_tag.get_text(strip=True) if title_tag else "N/A"

            # Status is inside a div with class "cb-ovr-flo cb-text-live"
            status_tag = match.find("div", class_="cb-ovr-flo cb-text-live")
            status = status_tag.get_text(strip=True) if status_tag else "Status not available"

            # Score is often in the sibling div following status or inside div with class 'cb-ovr-flo'
            # We try to find all divs with class 'cb-ovr-flo' in match, then pick text excluding status
            score = ""
            score_divs = match.find_all("div", class_="cb-ovr-flo")
            for div in score_divs:
                # Skip status div, take others as score
                if div != status_tag:
                    score += div.get_text(strip=True) + " "

            score = score.strip() if score else "Score not available"

            results.append({
                "title": title,
                "status": status,
                "score": score
            })

        return results
    except requests.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# For quick testing:
if __name__ == "__main__":
    from pprint import pprint
    pprint(get_live_scores())
