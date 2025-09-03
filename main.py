import uvicorn
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas.query import QueryRequest,QueryResponse
from app.chatbot import process_query


app = FastAPI(title="New Hire Onboarding Buddy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
    expose_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Headers"],
)

@app.get("/")
def home():
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
    }
    return JSONResponse(content={"message": "Chatbot API is running!"}, headers=headers)



@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest):
    response_text = process_query(request.query)
    return QueryResponse(response=response_text)


if __name__ == "__main__":
    uvicorn.run(app,port=8000)


