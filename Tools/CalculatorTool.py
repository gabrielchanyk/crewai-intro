from langchain_community.tools import tool

@tool("Calculate")
def calculate(equation):

    return eval(equation)
