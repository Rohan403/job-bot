import pandas as pd

from scraper_linkedin import scrape_linkedin
from scraper_indeed import scrape_indeed
from cover_letter_generator import generate_cover_letters
from notifier import send_email

print("Starting AI Job Agent...")

linkedin_jobs = scrape_linkedin()
indeed_jobs = scrape_indeed()

all_jobs = linkedin_jobs + indeed_jobs

df = pd.DataFrame(all_jobs)

# remove duplicates
df.drop_duplicates(subset=["title","company","location"], inplace=True)

# replace NaN links
df["link"] = df["link"].fillna("")

# convert links to Excel hyperlinks
df["link"] = df["link"].apply(
    lambda x: f'=HYPERLINK("{x}","Open Job")' if x.strip() != "" else ""
)

# filter relevant jobs
df = df[df["title"].str.contains(
    "frontend|react|javascript",
    case=False,
    na=False
)]

print("Jobs collected and saved")

# save Excel
df.to_excel("data/jobs.xlsx", index=False)

print("Excel file saved in data/jobs.xlsx")

# ✅ Generate cover letters
generate_cover_letters()

print("Cover letters generated")

# ✅ Send email
send_email()

print("Email notification sent")