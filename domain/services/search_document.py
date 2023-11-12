from typing import List, Optional
from domain.entities.document import Document
from domain.repositories.document_repository import DocumentRepository

class DocumentService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def get_all_documents(self, title: Optional[str] = None) -> List[Document]:
        return self.repository.get_all_documents(title)

    def get_document_by_id(self, id: int) -> Optional[Document]:
        return self.repository.get_document_by_id(id)