# VirtualStudy AI Marketing Agents

This application is an AI-powered marketing automation system designed for VirtualStudy.com. It uses [CrewAI](https://github.com/joaomdmoura/crewAI), [LangChain](https://www.langchain.com/), and [OpenAI GPT models](https://openai.com/) to coordinate intelligent agents responsible for tasks such as research, content creation, SEO, email marketing, and campaign management.

## Features

- **AI Agents for Marketing Tasks**  
  - Researcher: Gathers EdTech market trends and insights  
  - Content Creator: Writes articles and promotional material  
  - SEO Specialist: Optimizes content for search engines  
  - Email Marketer: Sends email campaigns to subscriber lists  
  - Marketing Manager: Oversees the whole campaign and consolidates results  

- **Crew-Based Coordination**  
  Agents are organized in a `Crew` to work collaboratively on a campaign.

- **Streamlit UI**  
  A simple interface allows you to run agents individually and download their output.

- **Email Campaign Integration**  
  The email marketer agent automatically sends newsletters to a mailing list (`emails.csv`) using SMTP with Gmail.

- **Downloadable Results**  
  Final agent output is available as a downloadable `.txt` file.

## Tech Stack

- Python 3.10+
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- CrewAI + LangChain + OpenAI
- ChromaDB (optional memory storage)
- Gmail SMTP for email delivery
- Dockerized deployment

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/virtualstudy-agents.git
cd virtualstudy-agents

2. Create Environment Variables
Create a .env file in the root with:
OPENAI_API_KEY=your_openai_api_key
SERPAPI_KEY = your_serpai_api_key
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password  # Use a Gmail app password

3. Prepare Your Email List
Create a file called emails.csv in the backend directory with a column email:

email
student1@example.com
parent2@example.com
schooladmin@example.com

4. Install Dependencies
pip install -r requirements.txt

Or use Docker:
docker-compose up --build

5. Run the App
Backend API:
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000

Frontend Streamlit UI:
cd frontend
streamlit run app.py

Future Improvements
Add Telegram posting for social media agent
Implement persistent memory via ChromaDB
Dashboard for analytics and performance metrics

License
MIT License

Credits
Built by Yitayew  with AI integrations to help revolutionize education access in Ethiopia.
