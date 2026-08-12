import requests
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = init_chat_model(
    "google_genai:gemini-3.1-flash-lite",
    temperature=0.1
)

conversation=[
    SystemMessage('You are a powerful agent'),
    HumanMessage('What is Python?'),
    AIMessage('Python is a interpreter language'),
    HumanMessage('When was it released?')
    ]
for ch in model.stream(conversation):
    print(ch.text,end=' ',flush=True)

