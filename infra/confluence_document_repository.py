import datetime
import requests
import json
import html2text
from typing import List, Optional
from domain.entities.document import Document

class ConfluenceRepository:
    def __init__(self, base_url: str, username: str, token: str):
        self.base_url = base_url
        self.username = username
        self.token = token

    def get_all_documents(self, title: Optional[str] = None) -> List[Document]:
        headers = {'Authorization': 'Bearer ' + self.token}
        print(f"{self.base_url}/rest/api/content/search?cql=" + title)
        response = requests.get(f"{self.base_url}/rest/api/content/search?cql=(type=page and text ~ \"{title}\")", headers=headers, verify=False)
        response.raise_for_status()
        documents = []
        for page in response.json()['results']:
            print(page)
            document = Document(
                id=page['id'], 
                title=page['title'], 
                lastChange=datetime.datetime.now(),
                content="",
                content_type='text/html', 
                location=f"{self.base_url}{page['_links']['webui']}"
            )
            documents.append(document)
        return documents

    def get_document_by_id(self, id: str) -> Optional[Document]:
        headers = {'Authorization': 'Bearer ' + self.token}
        response = requests.get(f"{self.base_url}/rest/api/content/{id}?expand=body.storage", headers=headers, verify=False)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        page = response.json()

        # Convert HTML content to markdown
        h = html2text.HTML2Text()
        markdown_content = h.handle(page['body']['storage']['value'])

        return Document(
            id=page['id'],
            title=page['title'],
            lastChange=datetime.datetime.now(),
            content=markdown_content,
            content_type='text/markdown',
            location=f"{self.base_url}{page['_links']['webui']}"
        )