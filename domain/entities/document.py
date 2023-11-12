from pydantic import BaseModel
from datetime import datetime

class Document(BaseModel):
    id: int
    title: str
    lastChange: datetime
    content: str
    content_type: str = "plain/text"


documents = [
    Document(id=1, title="Document 1", lastChange=datetime.now(), content="Content of Document 1", content_type="text/markdown"),
    Document(id=2, title="Document 2", lastChange=datetime.now(), content="Content of Document 2", content_type="text/markdown"),
]