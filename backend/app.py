from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from fastapi import FastAPI
from graph import workflow

app = FastAPI()
class ChatRequest(BaseModel):
    message: str


@app.post('/chat')
def chat(req : ChatRequest):
    result = workflow.invoke(
    {
        "messages": [
            HumanMessage(content=req.message)
        ]
    },
    config={
        "configurable": {
            "thread_id": "1"
        }
    }
)
    return {"response": result["messages"][-1].content}