import requests
from typing import List, Optional
from domain.entities.document import Document

class ConfluenceRepository:
    def __init__(self, base_url: str, username: str, token: str):
        self.base_url = base_url
        self.username = username
        self.token = token

    def get_all_documents(self, title: Optional[str] = None) -> List[Document]:
        documents = []
        response = requests.get(f"{self.base_url}/wiki/rest/api/content", auth=(self.username, self.token))
        response.raise_for_status()
        for page in response.json()['results']:
            if title is None or title.lower() in page['title'].lower():
                document = Document(id=page['id'], title=page['title'], lastChange=page['version']['when'], content_type='text/html', location=f"{self.base_url}/wiki/spaces/{page['space']['key']}/pages/{page['id']}")
                documents.append(document)
        return documents

    def get_document_by_id(self, id: str) -> Optional[Document]:
        response = requests.get(f"{self.base_url}/wiki/rest/api/content/{id}", auth=(self.username, self.token))
        if response.status_code == 404:
            return None
        response.raise_for_status()
        page = response.json()
        return Document(id=page['id'], title=page['title'], lastChange=page['version']['when'], content=page['body']['view']['value'], content_type='text/html', location=f"{self.base_url}/wiki/spaces/{page['space']['key']}/pages/{page['id']}")