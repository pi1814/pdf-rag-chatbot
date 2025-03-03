# PDF Chat with Retrieval-Augmented Generation (RAG)

## Steps:
1. Clone the project
2. Create a data folder with the required pdf files
3. Add necessary configuration like OpenAI API keys etc. in env file
4. Run script `data_export.py` with model options to load up ChromaDB (Vector Database)
5. Create a virtual environment: `python -m venv venv`
6. Install dependancies
7. Run command: `uvicorn main:app --reload`
8. Go to `localhost:8000/docs`
9. Interact with the API

# Running with Docker

Please note before running the docker commands, you should have the env config set properly.

Run the following command to build the docker image at the base of the repo:
```
docker build --tag 'pdf_chat_with_rag' .
```

Run the image with the following command:

```
docker run -p 8000:8000 pdf_chat_with_rag
```
