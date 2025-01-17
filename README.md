# crewai-intro

pip install crewai
pip install langchain_community

create agent, task and crew

Get open ai key:

platform.openai.com

- get key
- need to have $2

Attributes:
agent_executor: An instance of the CrewAgentExecutor class.
role: The role of the agent.
goal: The objective of the agent.
backstory: The backstory of the agent.
knowledge: The knowledge base of the agent.
config: Dict representation of agent configuration.
llm: The language model that will run the agent.
function_calling_llm: The language model that will handle the tool calling for this agent, it overrides the crew function_calling_llm.
max_iter: Maximum number of iterations for an agent to execute a task.
memory: Whether the agent should have memory or not.
max_rpm: Maximum number of requests per minute for the agent execution to be respected.
verbose: Whether the agent execution should be in verbose mode.
allow_delegation: Whether the agent is allowed to delegate tasks to other agents.
tools: Tools at agents disposal
step_callback: Callback to be executed after each step of the agent execution.
knowledge_sources: Knowledge sources for the agent.

5 core concepts:

1. Agent: Member of a team/crew
2. Tasks: something to be completed by agent
3. What helps the agent perform certain actions

- can use langchain tools to use in crew ai with crew ai tools

4. Process: how to orchestrate execution of tasks by agents

- 2 ways: sequential or hierachical (default is sequential)

5. Crew: collobrative group of agents working together to achieve a set of tasks
