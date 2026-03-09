from linkedin_jobs_api import query
from config import KEYWORDS, LOCATIONS, LIMIT

def scrape_linkedin():

    jobs = []

    for keyword in KEYWORDS:
        for location in LOCATIONS:

            results = query(
                keyword=keyword,
                location=location,
                limit=str(LIMIT),
                date_since_posted="past week"
            )

            for job in results:

                jobs.append({
                    "title": job.get("position", ""),
                    "company": job.get("company", ""),
                    "location": job.get("location", ""),
                    "link": job.get("jobUrl", ""),   # correct field
                    "source": "LinkedIn"
                })

    return jobs