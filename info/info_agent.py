import os
from crewai import Agent, Task, Crew

os.environ["OPENAI_API_KEY"] = "sk-proj-"
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
    You love to know information.
"""
)

task1 = Task(
    description="Tell me all about the blue-ringed octopus.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print(result)