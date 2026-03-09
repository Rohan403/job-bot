# 🤖 AI Job Agent

An automated **AI-powered job search assistant** that scrapes jobs from multiple platforms, filters relevant roles, generates cover letters, and sends job alerts directly to your email.

This project helps automate the job search process by collecting fresh job listings and organizing them into an Excel report while notifying the user via email.

---

## 🚀 Features

* 🔎 Scrapes jobs from multiple sources

  * LinkedIn
  * Indeed

* 🧹 Cleans and filters job listings

* 📊 Exports results to an Excel spreadsheet

* 🔗 Generates clickable job links

* ✉️ Sends automated job alerts via email

* 📝 Automatically generates cover letters

* ⚡ Designed as a lightweight **AI automation pipeline**

---

## 📂 Project Structure

```
job-bot/
│
├── main.py
├── scraper_linkedin.py
├── scraper_indeed.py
├── cover_letter_generator.py
├── notifier.py
├── config.py
│
├── data/
│   └── jobs.xlsx
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone git clone https://github.com/Rohan403/job-bot.git
cd job-bot
```

### 2️⃣ Install dependencies

```
pip install pandas requests beautifulsoup4 linkedin-jobs-api openpyxl
```

### 3️⃣ Configure Email

Edit `notifier.py` and add your Gmail and **App Password**.

```
sender_email = "your_email@gmail.com"
password = "your_gmail_app_password"
```

To generate an App Password:

1. Enable **2-Step Verification** in your Google account
2. Go to **Google → Security → App Passwords**
3. Create a password for **Mail**

---

## ▶️ Usage

Run the job agent:

```
python main.py
```

The script will:

1. Scrape jobs from LinkedIn and Indeed
2. Filter relevant frontend roles
3. Save results to Excel
4. Generate cover letters
5. Send an email with the job report

---

## 📧 Example Email Output

You will receive an email with:

* Latest job listings
* Job details (title, company, location)
* Excel file containing the full dataset

---

## 📊 Example Excel Output

| Title              | Company | Location | Link     |
| ------------------ | ------- | -------- | -------- |
| Frontend Developer | Shopify | Remote   | Open Job |
| React Developer    | Amazon  | Canada   | Open Job |

---

## 🧠 Future Improvements

Planned upgrades for the project:

* AI job-resume matching
* Daily automated job reports
* Additional job sources (Glassdoor, Wellfound)
* Dashboard for job tracking
* Intelligent ranking of job opportunities

---

## 🛠 Technologies Used

* Python
* Pandas
* BeautifulSoup
* Requests
* SMTP Email Automation
* Excel (OpenPyXL)

---

## 💡 Motivation

Searching for jobs manually across multiple platforms is time-consuming.
This project automates the process by collecting, filtering, and delivering job opportunities automatically.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Developed by **Niladri Pal**

If you like this project, consider giving it a ⭐ on GitHub.
