from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from fastapi import FastAPI
from graph import workflow
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post('/chat')
def chat(req : ChatRequest):
    print(req.message)
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