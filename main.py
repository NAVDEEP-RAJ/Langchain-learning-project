from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "google_genai:gemini-3.1-flash-lite",
    temperature=0.7
)

response = model.stream("What is LangChain?")

for chunk in response:
    print(chunk.text, end="")