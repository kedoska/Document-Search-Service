from pydantic import BaseModel
from datetime import datetime

class Document(BaseModel):
    id: int
    title: str
    lastChange: datetime
    content: str
    content_type: str = "plain/text"
    location: str = None
