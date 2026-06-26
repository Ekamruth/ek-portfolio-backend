import json
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.rag.generator import generate_response, generate_response_stream
from app.api.history import create_conversation, get_history, add_messages

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()


class ChatRequest(BaseModel):
    query: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    response: str
    conversation_id: str


@router.get("/conversation/{conversation_id}/history")
async def get_conversation_history(conversation_id: str):
    history = get_history(conversation_id)
    if not history:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return {"conversation_id": conversation_id, "history": history}


@router.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
async def chat(request: Request, body: ChatRequest):
    if not body.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    conversation_id = body.conversation_id or create_conversation()
    history = get_history(conversation_id)

    result = generate_response(body.query, history)

    add_messages(conversation_id, body.query, result.content)

    return ChatResponse(response=result.content, conversation_id=conversation_id)


@router.post("/chat/stream")
@limiter.limit("10/minute")
async def chat_stream(request: Request, body: ChatRequest):
    if not body.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    conversation_id = body.conversation_id or create_conversation()
    history = get_history(conversation_id)

    async def event_generator():
        full_response = ""
        yield f"data: {json.dumps({'type': 'conversation_start', 'conversation_id': conversation_id})}\n\n"

        for chunk in generate_response_stream(body.query, history):
            token = chunk.content
            if token:
                full_response += token
                yield f"data: {json.dumps({'type': 'text_delta', 'text': token})}\n\n"

        add_messages(conversation_id, body.query, full_response)
        yield f"data: {json.dumps({'type': 'message_end'})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
