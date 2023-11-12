from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.document import Document

class DocumentRepository(ABC):
    @abstractmethod
    def get_all_documents(self, title: Optional[str] = None) -> List[Document]:
        pass

    @abstractmethod
    def get_document_by_id(self, id: int) -> Optional[Document]:
        pass