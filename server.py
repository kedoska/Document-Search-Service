from fastapi import FastAPI
from typing import List
from domain.entities.document import Document
from domain.repositories.document_repository import DocumentRepository
# To run the application, use the command: uvicorn main:app --reloadfrom typing import List

app = FastAPI()



@app.get("/documents", response_model=List[Document])
def get_documents(title: str = None):
    return DocumentRepository.get_all_documents(title)

@app.get("/documents/{id}", response_model=Document)
def get_document(id: int):
    document = DocumentRepository.get_document_by_id(id)
    if document:
        return document
    return {"message": "Document not found"}