import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from CalculatorTool import calculate

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] =  os.getenv("OPENAI_MODEL_NAME")

print ("Welcome to Math Quiz")
math_input = input("What is your math equation: ")

math_agent = Agent(
   role="Math Magician",
   goal="You are able to evaluate any math equation",
   backstory="You are a math whiz",
   verbose=True,
   tools=[calculate]
)

writer = Agent(
    role="Writer",
    goal="Craft compelling explanations based from results of math equations",
    backstory="""
    You love to create and share fun math puzzles.
    """,
    verbose=True
)

task1 = Task(
    description=f"{math_input}",
    expected_output="Give full details of your math equation in bullet points",
    agent=math_agent
)

task2 = Task(
    description="Explain the results of your math equation",
    expected_output="Create a short story about your math equation",
    output_file="math.md",
    agent=writer
)

crew = Crew(
    agents=[math_agent, writer],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print(result)