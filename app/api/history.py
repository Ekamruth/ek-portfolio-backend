from uuid import uuid4

_store: dict[str, list[dict]] = {}

def create_conversation() -> str:
    conversation_id = str(uuid4())
    _store[conversation_id] = []
    return conversation_id

def get_history(conversation_id: str) -> list[dict]:
    return _store.get(conversation_id, [])

def add_messages(conversation_id: str, user_message: str, assistant_message: str) -> None:
    if conversation_id not in _store:
        _store[conversation_id] = []
    _store[conversation_id].append({"role": "user", "content": user_message})
    _store[conversation_id].append({"role": "assistant", "content": assistant_message})
