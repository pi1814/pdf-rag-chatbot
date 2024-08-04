from fastapi import FastAPI
from pydantic import BaseModel
from ChatbotHandler import ChatbotHandler

class QueryModel(BaseModel):
    query: str | None = None
    model: str | None = None
    text: str | None = None

app = FastAPI()

@app.post("/retrieve")
async def retrieve_from_doc(query: QueryModel):
    chatbot = ChatbotHandler()
    if query.model != None and query.model in ("mistral", "openai", "google"):
        chatbot = ChatbotHandler(query.model)
    return chatbot.retrieve(query.query)

@app.post("/summarize")
async def summarize_text(text: QueryModel):
    chatbot = ChatbotHandler()
    if text.model != None and text.model in ("mistral", "openai", "google"):
        chatbot = ChatbotHandler(text.model)
    return chatbot.summarize(text.text)

@app.post("/retrieve_and_summarize")
async def retrive_summarize_from_doc(query: QueryModel):
    chatbot = ChatbotHandler()
    if query.model != None and query.model in ("mistral", "openai", "google"):
        chatbot = ChatbotHandler(query.model)
    return chatbot.retrieve_and_summarize(query.query)