from crewai import Crew, Process
from tools import web_tool
from agents import social
from tasks import response_task
from dotenv import load_dotenv

load_dotenv()

crew1 = Crew(
    agents=[social],
    tasks=[response_task],
    process=Process.sequential,
    memory=True,
    cache=False,
    max_rpm=100,
    share_crew=True
)

result=crew1.kickoff({"question":"What does Social Hardware do?"})
print(result)