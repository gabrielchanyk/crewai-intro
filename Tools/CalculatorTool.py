from langchain.tools import tool

@tool("Calculate")
def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns the result.
    
    Args:
    expression (str): A string containing a mathematical expression to be evaluated.
    
    Returns:
    str: The result of the evaluated expression as a string.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"