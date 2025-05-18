import smtplib
from email.mime.text import MIMEText
from crewai import Agent
from langchain_openai import ChatOpenAI
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, content):
    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    df = pd.read_csv("emails.csv")  
    to_emails = df['email'].dropna().tolist()

    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(to_emails)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_emails, msg.as_string())
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def create_email_marketer():
    def run():
        subject = "EdTech Weekly Trends - Insights from VirtualStudy.com"
        content = (
            "Greetings from VirtualStudy.com!\n\n"
            "Here's your weekly newsletter featuring the latest EdTech developments, study tips, and updates to help students, parents, and schools succeed.\n\n"
            "Stay inspired and keep learning!"
        )
        success = send_email(subject, content)
        if success:
            return "✅ Email campaign executed and sent successfully."
        else:
            return "❌ Failed to send email campaign."

    return Agent(
        role="Email Marketing Specialist",
        goal="Create and send optimized email campaigns to VirtualStudy.com's subscribers.",
        backstory=(
            "You are a seasoned email marketer managing newsletters and campaigns for VirtualStudy.com. "
            "You understand educational audiences and deliver culturally relevant and personalized email content."
        ),
        verbose=True,
        llm=ChatOpenAI(),
        run=run,
        instructions=[
            "Segment audiences by type, behavior, and location.",
            "Use compelling subject lines, concise content, and localized messaging.",
            "Keep emails mobile-optimized and easy to read.",
            "Include strong CTAs such as 'Start Learning Now' or 'Join a Free Class'."
        ]
    )
