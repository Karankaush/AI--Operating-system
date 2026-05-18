from pydantic import BaseModel
from fastapi import FastAPI
from graph import graph_test

app = FastAPI()
class ChatRequest(BaseModel):
    message: str


@app.post('/chat')
def chat(req : ChatRequest):
    result = graph_test.invoke({
        "user_message": req.message
    })
    return {"response": result}