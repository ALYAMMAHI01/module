pip install langchain langchain-openai

from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
import math

def calculator(expression: str) -> str:
    """
    Evaluates a math expression safely
    """
    try:
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs
        }
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

math_tool = Tool(
    name="Calculator",
    func=calculator,
    description=(
        "Use this tool for ALL math operations. "
        "Input must be a valid math expression, e.g. '2 + 3 * 4', 'sqrt(16)', 'pow(2,3)'."
    )
)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


agent = initialize_agent(
    tools=[math_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


questions = [
    "What is 25 * 4?",
    "What is the square root of 144?",
    "If I buy 3 items for $19.99 each, how much do I pay?",
    "What is (5 + 3) ^ 2?"
]

for q in questions:
    print(f"\n❓ {q}")
    answer = agent.run(q)
    print(f" Answer: {answer}")
