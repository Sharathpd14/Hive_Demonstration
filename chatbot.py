from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Query(BaseModel):
    question: str

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.post("/ask")  
@app.get("/ask")   
async def ask_chatbot(query: Query = None):
    if not query:
        return {"message": "Send a question using POST request."}

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": query.question}],
        model="gemma2-9b-it",
    )

    return {"response": chat_completion.choices[0].message.content}
