import os
from fastapi import FastAPI
from typing import List
from domain.entities.document import Document
from domain.services.search_document import DocumentService
from infra.local_document_repository import LocalDocumentRepository
from infra.confluence_document_repository import ConfluenceRepository

app = FastAPI()

# Read the DOCUMENT_SOURCE environment variable
document_source = os.getenv("DOCUMENT_SOURCE")

# Decide which repository to use based on DOCUMENT_SOURCE
if document_source == "confluence":
    # Read the CONFLUENCE_BASE_URL, CONFLUENCE_USERNAME and CONFLUENCE_TOKEN environment variables
    confluence_base_url = os.getenv("CONFLUENCE_BASE_URL")
    confluence_username = os.getenv("CONFLUENCE_USERNAME")
    confluence_token = os.getenv("CONFLUENCE_TOKEN")
    # Initialize the ConfluenceRepository with the environment variables
    repository = ConfluenceRepository(confluence_base_url, confluence_username, confluence_token)
else:
    # Read the DOCUMENT_DIRECTORY environment variable
    document_directory = os.getenv("DOCUMENT_DIRECTORY")
    repository = LocalDocumentRepository(document_directory)

# Initialize the DocumentService with the chosen repository
document_service = DocumentService(repository)

@app.get("/documents", response_model=List[Document])
def get_documents(title: str):
    return document_service.get_all_documents(title)

@app.get("/documents/{id}", response_model=Document)
def get_document(id: str):
    document = document_service.get_document_by_id(id)
    if document:
        return document
    return {"message": "Document not found"}