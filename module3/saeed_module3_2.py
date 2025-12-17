
# FastAPI application that handles POST requests to /message endpoint.
# It validates the incoming JSON payload to ensure it contains a non-empty "Text" field.
# If valid, it responds with the same text and a timestamp; otherwise, it returns a 422 error.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class MessageRequest(BaseModel):
    Text: str

class MessageResponse(BaseModel):
    Text: str
    timestamp: str

@app.post("/message", response_model=MessageResponse)
async def post_message(request: MessageRequest):
    if not request.Text or not request.Text.strip():
        raise HTTPException(status_code=422, detail={"error": "Text field is missing or empty"})
    timestamp = datetime.now().isoformat()
    return MessageResponse(Text=request.Text, timestamp=timestamp)


