from crewai import Agent
#from langchain.chat_models import ChatOpenAI
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

def create_researcher():
    return Agent(
        role="Researcher",
        goal="Find and summarize the latest marketing trends for EdTech in Ethiopia",
        backstory="Web-based research expert.",
        verbose=True,
        llm=ChatOpenAI()
    )


# from crewai import Agent
# from langchain_openai import ChatOpenAI

# def create_researcher():
#     return Agent(
#         role="EdTech Market Research Analyst",
#         goal=(
#             "Conduct comprehensive, up-to-date research on marketing trends in the Ethiopian EdTech industry. "
#             "Generate a structured report highlighting current strategies, digital marketing channels, competitor analysis, "
#             "successful campaigns, government initiatives, mobile learning adoption, social media behavior, and internet penetration in Ethiopia."
#         ),
#         backstory=(
#             "You are an expert market research analyst with deep knowledge of global and African EdTech trends. "
#             "You specialize in identifying and analyzing educational technology developments in emerging markets, particularly Ethiopia. "
#             "You are skilled in synthesizing large volumes of web-based information into concise and insightful summaries that inform business strategy. "
#             "Your research powers the decision-making of marketing managers and startup founders looking to expand in the education sector."
#         ),
#         verbose=True,
#         llm=ChatOpenAI(),
#         instructions=[
#             "Search for authoritative sources such as UNESCO, World Bank, Ethiopian Ministry of Education, and news outlets like The Reporter Ethiopia or Addis Fortune.",
#             "Summarize the top 5 most relevant and recent marketing trends in EdTech in Ethiopia.",
#             "Include statistics where available: internet/mobile penetration rates, education access, demographics, etc.",
#             "List the most commonly used digital platforms and channels (e.g., Facebook, Telegram, YouTube, SMS) for educational marketing.",
#             "Identify at least 3 successful EdTech marketing campaigns or companies in Ethiopia and explain their strategies.",
#             "Highlight any government regulations, national strategies, or policy shifts that affect EdTech marketing.",
#             "Note the preferred languages and cultural practices that impact marketing effectiveness in Ethiopia.",
#             "Provide a short section summarizing marketing challenges and opportunities unique to the Ethiopian context.",
#             "Structure your findings into sections with clear titles and bullet points for easy consumption.",
#             "Avoid generic advice—focus specifically on localized, actionable insights for Ethiopia’s EdTech space."
#         ]
#     )
