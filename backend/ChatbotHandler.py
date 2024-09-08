from backend.DocumentRetriever import DocumentRetriever
from backend.ModelHandler import ModelHandler
from langchain.prompts import ChatPromptTemplate

retrieve_and_summarize_prompt_template = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}

"""
GENERIC_RESPONSE = """I'm not sure about this. The query has nothing to do with the context."""

EVAL_PROMPT = """
Context: {context}
Response: {actual_response}
---
(Answer with 'true' or 'false') Does the response based on the context? 
"""

class ChatbotHandler():
    def __init__(self, model_name="mistral"):
        self.document_retriver = DocumentRetriever(model_name)
        self.model_handler = ModelHandler(model_name)
    
    def retrieve(self, query:str):
        return {"documents": self.document_retriver.retrieve(query)}
    
    def summarize(self, text:str):
        return self.model_handler.get_summary(text)
    
    def retrieve_and_summarize(self, query:str):
        documents =  self.document_retriver.retrieve(query)
        context = "\n\n---\n\n".join([doc.page_content for doc, _score in documents])
        prompt_template = ChatPromptTemplate.from_template(retrieve_and_summarize_prompt_template)
        prompt = prompt_template.format(context=context, question=query)
        response = self.model_handler.retrieve_docs_summary(query, prompt)
        # if self.query_and_validate(response, context) is False:
        #     return {"documents": documents, "response": GENERIC_RESPONSE}
        return {"documents": documents, "response": response}
     
    def query_and_validate(self, response_text: str, context: str):
        prompt = EVAL_PROMPT.format(
            actual_response=response_text,
            context=context
        )
        evaluation_results_str = self.model_handler.retrieve_docs_summary(response_text, prompt)
        evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

        print(prompt)

        if "true" in evaluation_results_str_cleaned:
            # Print response in Green if it is correct.
            print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
            return True
        elif "false" in evaluation_results_str_cleaned:
            # Print response in Red if it is incorrect.
            print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
            return False
        else:
            raise ValueError(
                f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
            )