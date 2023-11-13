import os
import mimetypes
from typing import List, Optional
from domain.entities.document import Document

class LocalDocumentRepository:
    def __init__(self,  directory: str):
        self.directory = directory

    def get_all_documents(self,title: Optional[str] = None) -> List[Document]:
        documents = []
        for filename in os.listdir(self.directory):
            # check if file is file and not directory
            if os.path.isfile(os.path.join(self.directory, filename)):
                if title is None or title.lower() in filename.lower():
                    with open(os.path.join(self.directory, filename), 'r') as f:
                        content = f.read()
                        content_type = 'text/plain'
                        document = Document(id=filename, title=filename, lastChange=os.path.getmtime(os.path.join(self.directory, filename)), content="", content_type=content_type, location=f"/documents/{filename}")
                        documents.append(document)
        return documents

    def get_document_by_id(self, title: str) -> Optional[Document]:
        for filename in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, filename)):
                if filename.lower() == title.lower():
                    with open(os.path.join(self.directory, filename), 'r') as f:
                        content = f.read()
                        content_type = 'text/plain'
                        return Document(id=filename, title=filename, lastChange=os.path.getmtime(os.path.join(self.directory, filename)), content=content, content_type=content_type, location=f"/documents/{filename}")
        return None