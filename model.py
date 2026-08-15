import requests
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


model = init_chat_model(
    "google_genai:gemini-3.1-flash-lite",
    temperature=0.7
)
response=model.stream('What is the Langchain ')
for i in response:
    print(i.text,end=' ')
