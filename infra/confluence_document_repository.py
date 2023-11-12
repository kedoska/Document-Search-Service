import requests
from typing import List, Optional
from domain.entities.document import Document

class ConfluenceRepository:
    @staticmethod
    def get_all_documents(base_url: str, username: str, token: str, title: Optional[str] = None) -> List[Document]:
        documents = []
        response = requests.get(f"{base_url}/wiki/rest/api/content", auth=(username, token))
        response.raise_for_status()
        for page in response.json()['results']:
            if title is None or title.lower() in page['title'].lower():
                document = Document(id=page['id'], title=page['title'], lastChange=page['version']['when'], content=page['body']['view']['value'], content_type='text/html')
                documents.append(document)
        return documents

    @staticmethod
    def get_document_by_id(base_url: str, username: str, token: str, id: str) -> Optional[Document]:
        response = requests.get(f"{base_url}/wiki/rest/api/content/{id}", auth=(username, token))
        if response.status_code == 404:
            return None
        response.raise_for_status()
        page = response.json()
        return Document(id=page['id'], title=page['title'], lastChange=page['version']['when'], content=page['body']['view']['value'], content_type='text/html')