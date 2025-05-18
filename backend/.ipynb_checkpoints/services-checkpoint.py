from crewai import Crew, Task
from backend.utils.memory_store import log_agent_run
from backend.agents.researcher_agent import create_researcher
from backend.agents.content_creator_agent import create_content_creator
# from backend.agents.seo_specialist import create_seo_specialist
# from backend.agents.graphic_designer import create_graphic_designer
from backend.agents.social_media_manager import create_social_media_manager
from backend.agents.email_marketer import create_email_marketer
# from backend.agents.analyst import create_analyst
# from backend.agents.product_marketer import create_product_marketer
from backend.agents.marketing_manager import create_marketing_manager

def run_all_agents():
    agents = [
        create_researcher(), create_content_creator(), create_seo_specialist(),
        create_graphic_designer(), create_social_media_manager(),
        create_email_marketer(), create_analyst(),
        create_product_marketer(), create_marketing_manager()]

    tasks = [
        Task(description="Research market trends", expected_output="Insight Summary", agent=agents[0]),
        Task(description="Create content", expected_output="Blog and posts", agent=agents[1]),
        #Task(description="Optimize SEO", expected_output="Keyword plan", agent=agents[2]),
        #Task(description="Design visuals", expected_output="Graphics pack", agent=agents[3]),
        Task(description="Manage social media", expected_output="Get content from the content creator and Posting schedule", agent=agents[4]),
        Task(description="Email campaign", expected_output="Newsletter draft and send email", agent=agents[5]),
        #Task(description="Analyze KPIs", expected_output="Performance dashboard", agent=agents[6]),
        #Task(description="Go-to-market", expected_output="Launch strategy", agent=agents[7]),
        Task(description="Review all", expected_output="Campaign plan", agent=agents[8])]

    crew = Crew(agents=agents, tasks=tasks)
    result = crew.kickoff()

    # ✅ Format result and save to file
    if isinstance(result, dict) and "tasks_output" in result:
        full_output = "\n\n".join(
            f"Agent: {task.get('agent', 'N/A')}\nTask: {task.get('description', 'N/A')}\n\n{task.get('raw', '')}"
            for task in result["tasks_output"]
        )
    else:
        full_output = str(result)

    # ✅ Save to file
    output_path = "/app/data/all_agents_output.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(full_output)

    log_agent_run("crew", result)
    return result

def run_agent_by_name(name):
    agent_map = {
        "Researcher": create_researcher,
        "Content Creator": create_content_creator,
        #"seo": create_seo_specialist,
        #"designer": create_graphic_designer,
        "Social Media Manager": create_social_media_manager,
        "Email Marketer": create_email_marketer,
        #"analyst": create_analyst,
        #"product": create_product_marketer,
        "Manager": create_marketing_manager
    }
    agent_func = agent_map.get(name)
    if not agent_func:
        return f"No such agent: {name}"
    agent = agent_func()
    task = Task(
        description="Perform your specific job as an AI marketing agent.",
        expected_output="Agent Output",
        agent=agent
    )
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    log_agent_run(name, result)
    return result

