import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


@tool(
    "get_weather",
    description="Return the weather information for a given city",
    return_direct=False
)
def weather(city: str):
    response = requests.get(
        f"https://wttr.in/{city}?format=j1"
    )
    return response.json()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)


agent = create_agent(
    model=llm,
    tools=[weather],
    system_prompt="You are a helpful assistant who always cracks jokes"
)


response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the weather like in Mumbai?"
            }
        ]
    }
)


print(response)
print(response["messages"][-1].content)

