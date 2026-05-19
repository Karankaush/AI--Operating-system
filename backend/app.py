from pydantic import BaseModel
from fastapi import FastAPI
from graph import workflow

app = FastAPI()
class ChatRequest(BaseModel):
    message: str


@app.post('/chat')
def chat(req : ChatRequest):
    result = workflow.invoke({
        "user_message": req.message
    })
    return {"response": result}