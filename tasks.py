from crewai import Task
from tools import web_tool

response_task=Task(
    agent=social,
    description="Read the data in the website and answer the following question {question}",
    tools=[web_tool,]
)