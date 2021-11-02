from typing import List
from eliza import Eliza
from fastapi import FastAPI
from pydantic import BaseModel

class Conversation(BaseModel):
    utterances: List[str]

app = FastAPI()
eliza = Eliza()
eliza.load('doctor.txt')

@app.get("/")
def index():
    return "hello world"

@app.get("/name")
def name():
    return "Eliza"

@app.post("/converse")
def converse(conversation: Conversation):
    eliza.memory = []
    for utterance in conversation.utterances:
        answer = eliza.respond(utterance)
    return answer
