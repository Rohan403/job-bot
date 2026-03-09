import pandas as pd

def generate_cover_letters():

    df = pd.read_excel("data/matched_jobs.xlsx")

    for _, row in df.head(5).iterrows():

        letter = f"""
Dear {row['company']} Hiring Manager,

I am excited to apply for the {row['title']} role at {row['company']}.

My experience in frontend development with JavaScript, React, HTML, and CSS
makes me a strong candidate for this position.

I would welcome the opportunity to contribute to your team.

Best regards
Your Name
"""

        filename = f"data/cover_letter_{row['company']}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(letter)

    print("Cover letters generated")