from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import OpenAI

prompt_template = """Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:"""

class ModelHandler():
    def __init__(self, model_name:str):
        self.model = model_name
    
    def load_model(self):
        load_dotenv()
        model = Ollama(model="mistral")
        if self.model == "openai":
            model = OpenAI()
        elif self.model == "google":
            model = GoogleGenerativeAI(model="models/text-bison-001")
        return model
    
    def get_summary(self, text:str):
        model = self.load_model()
        prompt_template = PromptTemplate.from_template(prompt_template)
        prompt = prompt_template.format(text=text)
        response_text = model.invoke(prompt)
        return response_text
    
    def retrieve_docs_summary(self, query:str, prompt):
        model = self.load_model()
        response_text = model.invoke(prompt)
        return response_text