import requests
from bs4 import BeautifulSoup

def get_live_scores():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    matches = []

    for match in soup.find_all("div", class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm"):
        title = match.find("a").text.strip()
        status = match.find("div", class_="cb-lv-scrs-col").text.strip()
        summary = match.find("div", class_="cb-text-live" or "cb-text-complete" or "cb-text-preview")

        matches.append({
            "title": title,
            "status": status,
            "summary": summary.text.strip() if summary else ""
        })

    return matches
