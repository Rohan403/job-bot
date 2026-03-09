import pandas as pd

def generate_cover_letters():

    df = pd.read_excel("data/matched_jobs.xlsx")

    for _, row in df.head(20).iterrows():

        letter = f"""
Dear {row['company']} Hiring Manager,

I’m excited to apply for the {row['title']} position at {row['company']}. With 3.8+ years of experience as a Full-Stack Web Developer specializing in the MERN stack, I have built and scaled production-grade applications across healthcare, fintech, and AI communication platforms. I am passionate about creating high-performance web applications that deliver seamless user experiences and real business impact.

In my current role as Senior Frontend Developer at Octopus Technologies, I improved application load time by 40% through advanced code-splitting and lazy loading, while architecting scalable state management systems supporting 10,000+ concurrent users. I also implemented JWT authentication and real-time communication using Socket.IO, enabling AI-powered voice agents to handle multilingual requests with sub-200ms latency.

Previously at Hyscalar, I helped build Doctegrity, a telemedicine platform used by 10,000+ patients, integrating Twilio Video APIs for secure real-time consultations with 99.5% session uptime. I also contributed to backend services using Node.js, Express, and MongoDB, designing REST APIs and scalable architectures that processed thousands of transactions daily.

Beyond my professional work, I actively build backend systems and automation tools, including finance APIs and event management platforms, focusing on modular architecture, security, and scalability.

I am particularly excited about the opportunity at {row['company']} because of your work in building impactful technology products, and I would love to contribute my experience in React, Node.js, scalable architectures, and performance optimization to help your team deliver exceptional products.

Thank you for your time and consideration. I look forward to the possibility of discussing how my skills and experience can contribute to your team.

Best regards,
Niladri Pal
Senior Full-Stack Developer

Email: niladripal160@gmail.com

Phone: +91 95569 03109
"""

        filename = f"data/cover_letter_{row['company']}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(letter)

    print("Cover letters generated")