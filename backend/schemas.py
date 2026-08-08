from pydantic import BaseModel


class ChatMessage(BaseModel):
    sender: str
    text: str


class ChatRequest(BaseModel):
    query: str
    history: list[ChatMessage] = []


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
