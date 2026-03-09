import pandas as pd

def match_jobs():

    jobs = pd.read_excel("data/jobs.xlsx")

    with open("data/resume.txt") as f:
        resume = f.read().lower()

    matched = []

    for _, job in jobs.iterrows():

        score = 0

        if "react" in resume and "react" in job["title"].lower():
            score += 1

        if "frontend" in job["title"].lower():
            score += 1

        if score >= 1:
            matched.append(job)

    df = pd.DataFrame(matched)

    df.to_excel("data/matched_jobs.xlsx", index=False)

    print("Matched jobs saved")