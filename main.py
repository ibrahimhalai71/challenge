from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReverseStr(BaseModel):
    input_string: str


@app.post("/reverse")
async def reverse_string(reverseStr: ReverseStr):
    return reverseStr.input_string[::-1]