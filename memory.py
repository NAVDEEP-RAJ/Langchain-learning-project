print("MEMORY.PY STARTED")

import requests


from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from dataclasses import dataclass
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver




load_dotenv()

@dataclass
class Context:
    user_id:str

@dataclass
class ResponseFormat:
    summary: str
    temperature_celcius:float
    humidity:float 


@tool('get_weather', description='Return weather information for a given city', return_direct=False)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

@tool("locate_user",description="Locate the user's location")
def locate_user(runtime:ToolRuntime[Context]):
    match runtime.context.user_id:
        case 'Navdy':
            return 'Coimbatore'
        case 'John':
            return 'Chennai'
        case 'Joseph':
            return 'Bangalore'
        case _:
            return 'Unknown location'
        
        
    

model = init_chat_model("google_genai:gemini-3.1-flash-lite",
                         temperature=0.3)
checkpointer=InMemorySaver()

agent = create_agent(
model = model,
tools = [get_weather,locate_user],
system_prompt = 'You are a helpful weather assistant, who always cracks jokes and is humorous while remaining helpful.',
context_schema=Context,                     #dataclass of out context
response_format=ResponseFormat,             #dataclass of ou ResponseFormat
checkpointer=checkpointer                   #Checkpointer to save the convo 
)

config={'configurable':{'thread_id':1}}
response = agent.invoke({
'messages' :[
{'role': 'user', 'content': 'What is the weather like?'}]},
 config=config,
 context=Context(user_id='Navdy')
)
result = response["structured_response"]

print(result.summary)
print(result.humidity)
print(result.temperature_celcius)
