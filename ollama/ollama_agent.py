import os
from crewai import Task, Crew, Process, Agent, LLM
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-1111"


llm =LLM(model="ollama/phi3:3.8b")
# llm = ChatOpenAI(
#     model="phi3:3.8b",
#     base_url="http://localhost:11434/v1"
# )
# llm2 = ChatOpenAI(
#     model="phi3:3.14b",
#     base_url="http://localhost:11434/v1"
# )

info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
    You love to know information.
    """,
    llm=llm
)

task1 = Task(
    description="Tell me all about the box jellyfish.",
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