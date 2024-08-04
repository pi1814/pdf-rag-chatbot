from langchain_chroma import Chroma
from embedding_func import get_google_embedding_function, get_openai_embedding_function

CHROMA_PATH = "chroma"

class DocumentRetriever():
    def __init__(self, model="mistral"):
        self.documents = list
        self.model = model
    
    def retrieve(self, query):
        embedding_function = get_google_embedding_function()
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
        results = db.similarity_search_with_score(query, k=5)
        self.documents = results
        return self.documents