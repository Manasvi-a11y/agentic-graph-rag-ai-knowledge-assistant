from fastapi import APIRouter, Depends, HTTPException

from backend.schemas import ChatRequest, ChatResponse
from backend.dependencies import get_agent

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    agent=Depends(get_agent)
):
    try:
        result = agent.chat(
            request.query,
            request.history,
        )

        return ChatResponse(
            answer=result["answer"],
            sources=result["sources"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )