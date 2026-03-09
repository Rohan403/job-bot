import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email():

    sender_email = "niladripal160@gmail.com"
    receiver_email = "niladripal160@gmail.com"
    password = "oejrocscksekcqbx"

    df = pd.read_excel("data/jobs.xlsx")

    job_list = ""

    for _, row in df.head(5).iterrows():

        job_list += f"""
Title: {row['title']}
Company: {row['company']}
Location: {row['location']}

-------------------------
"""

    subject = "New Frontend Jobs Found 🚀"

    body = f"""
Hello,

Here are some new jobs found by your AI Job Agent:

{job_list}

The full job list is attached as an Excel file.
"""

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    # 📎 attach Excel file
    filename = "data/jobs.xlsx"

    attachment = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename=jobs.xlsx"
    )

    message.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message.as_string())

    server.quit()

    print("Email sent with Excel attachment")