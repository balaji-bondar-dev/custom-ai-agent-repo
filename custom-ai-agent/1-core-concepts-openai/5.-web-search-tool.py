from openai import OpenAI
from agents import function_tool,Agent


client = OpenAI()

# Web Search Tool
answer = client.responses.create(
    model="gpt-5.5",
    input="Who is the current president of India?",
    tools=[{"type": "web_search"}]
)
print(answer.output_text)


# Wrap local logic as a function tool
@function_tool
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is sunny."

tools_list = [get_weather]

answer = client.responses.create(
    model="gpt-5.5",
    input="How is the weather in Paris today?",
    tools=tools_list,
    tool_choice= "auto",
)
print(answer.output_text)


