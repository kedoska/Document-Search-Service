import os
import mimetypes
from typing import List, Optional
from domain.entities.document import Document

class LocalDocumentRepository:
    @staticmethod
    def get_all_documents(directory: str, title: Optional[str] = None) -> List[Document]:
        documents = []
        for filename in os.listdir(directory):
            if title is None or title.lower() in filename.lower():
                with open(os.path.join(directory, filename), 'r') as f:
                    content = f.read()
                    content_type = mimetypes.guess_type(filename)[0]
                    document = Document(id=None, title=filename, lastChange=os.path.getmtime(os.path.join(directory, filename)), content=content, content_type=content_type)
                    documents.append(document)
        return documents

    @staticmethod
    def get_document_by_title(directory: str, title: str) -> Optional[Document]:
        for filename in os.listdir(directory):
            if filename.lower() == title.lower():
                with open(os.path.join(directory, filename), 'r') as f:
                    content = f.read()
                    content_type = mimetypes.guess_type(filename)[0]
                    return Document(id=None, title=filename, lastChange=os.path.getmtime(os.path.join(directory, filename)), content=content, content_type=content_type)
        return None