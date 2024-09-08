# PDF_CHAT_WITH_RAG

## Steps:
1. Clone the project
2. Change directory to backend directory
3. Create a data folder with the required pdf files
4. Add necessary configuration like OpenAI API keys etc. in env file
5. Run script `data_export.py` with model options to load up ChromaDB (Vector Database)
6. Create a virtual environment: `python -m venv venv`
7. Install dependancies
8. Run command: `uvicorn main:app --reload`
9. Go to `localhost:8000/docs`
10. Interact with the API
