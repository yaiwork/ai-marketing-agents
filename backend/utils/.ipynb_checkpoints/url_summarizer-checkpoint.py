import requests
import os
from openai import OpenAI
from bs4 import BeautifulSoup

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_url(url):
    try:
        html = requests.get(url, timeout=20).text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()[:4000]
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Summarize this webpage content:"},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error summarizing {url}: {e}"
