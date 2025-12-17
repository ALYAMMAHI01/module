# module3/saeed_module3_1.py
# A simple FastAPI application that accepts a POST request with a message
# and responds with the same message along with a timestamp.
# To run this application, use the command:
# uvicorn module3.saeed_module3_1:app --reload
# Then access the endpoint at http://
# localhost:8000/message
# Example POST request body:
# {#   "message": "Hello, World!"
# }
# Example response body:
# {#   "message": "Hello, World!",
#   "timestamp": "2024-06-01T12:34:56.789123"
# }
# Make sure to install FastAPI and Uvicorn if you haven't already:
# pip install fastapi uvicorn
# You can test the endpoint using curl or any API testing tool like Postman.
# curl -X POST "http://localhost:8000/message" -H "Content-Type: application/json" -d '{"message": "Hello, World!"}'
# The response will include the original message and the current timestamp.

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    message: str
    timestamp: str

@app.post("/message", response_model=MessageResponse)
async def post_message(request: MessageRequest):
    timestamp = datetime.now().isoformat()
    return MessageResponse(message=request.message, timestamp=timestamp)


   
