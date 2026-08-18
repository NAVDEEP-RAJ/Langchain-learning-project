from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model("google_genai:gemini-3.1-flash-lite")

message={
'role':'user',
'content':[
    {'type':'text','text':'what is there in the image and it"s significance'},
    {'type':'image','url':'https://www.google.com/imgres?q=batman&imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BMmU5NGJlMzAtMGNmOC00YjJjLTgyMzUtNjAyYmE4Njg5YWMyXkEyXkFqcGc%40._V1_.jpg&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1877830%2F&docid=P8oc_FAgsQvDHM&tbnid=fxonU1oXHUceGM&vet=12ahUKEwjp79GkoqqWAxUdlOEIHWtsEQEQnPAOegQIOhAA..i&w=2764&h=4096&hcb=2&ved=2ahUKEwjp79GkoqqWAxUdlOEIHWtsEQEQnPAOegQIOhAA'}

    ]

}
response=model.invoke([message])
print(response.content[0].get('text'))
