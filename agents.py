from crewai import Agent, LLM
from tools import web_tool
import os

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

llm = LLM(model="groq/gemma2-9b-it",api_key=api_key)

social=Agent(
    role="To read the content of the website and answer the query of the user.",
    goal="Answer the following question: {question}, based on the information provided by the website",
    backstory="You're an interactive AI chatbot for Social Hardware International, a tele-robotic company that specializes in developing custom VR operated telerobots for various bsuinesses",
    tools=[web_tool],
    llm=llm,
    memory=True,
    verbose=True
)