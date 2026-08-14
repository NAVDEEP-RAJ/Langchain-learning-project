import requests
from dtaclasses import dataclass
from langchsin.chat_models import init_chat_model
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.chechpoint.memory import InMemorysaver



load_dotenv()

@dataclass
class Context:
    user_id:str

@dataclass
class ResponseFormat:
    summary:str
    temperature_celcius:float
    temperature_farenheit:float
    humidity:float



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

@tool('locate_user',description="Look up a user's city based on the context")
def locate_user(runtime:toolRuntime[Context]):
    match runtime.context.user_id:
        case"ABC123" return 'Vietnam'


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

