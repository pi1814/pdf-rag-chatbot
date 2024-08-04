from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv


def get_google_embedding_function():
    load_dotenv()
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings

def get_openai_embedding_function():
    load_dotenv()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    return embeddings

def get_ollama_embedding_function():
    embeddings =  OllamaEmbeddings(model="mxbai-embed-large")
    return embeddings