import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

class QueryRequest(BaseModel):
    prompt: str

@app.post("/query")
async def query_openai(request: QueryRequest):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not set")
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8088, reload=True)
