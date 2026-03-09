import requests
from bs4 import BeautifulSoup

def scrape_indeed():

    jobs = []

    url = "https://www.indeed.com/jobs?q=frontend+developer"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    for card in soup.select(".job_seen_beacon")[:10]:

        title = card.select_one("h2.jobTitle")
        company = card.select_one(".companyName")
        location = card.select_one(".companyLocation")
        link_tag = card.select_one("a")

        job_link = ""
        if link_tag and link_tag.get("href"):
            job_link = "https://www.indeed.com" + link_tag.get("href")

        jobs.append({
            "title": title.text.strip() if title else "",
            "company": company.text.strip() if company else "",
            "location": location.text.strip() if location else "",
            "link": job_link,
            "source": "Indeed"
        })

    return jobs