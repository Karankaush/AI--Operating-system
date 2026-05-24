from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from fastapi import FastAPI
from graph import workflow
from fastapi import UploadFile, File
import shutil
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


@app.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"


    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename
    }

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