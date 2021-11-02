# Computing101

The goal of the session is to introduce you to the world of servers and APIs. At the end of the session, you will have built your own chatbot and will host it on a live server.

## Takeaways
1. Discover the world of servers
2. Learn about APIs
3. Commercial APIs available for NLP tasks

## 1. Connect to the server

1. Connect to the server using: https://sshwifty.herokuapp.com/
2. Your username is the concatenation of the letter "u" and your student ID: u<STUDENT_ID>
3. The password is the same for all accounts and will be displayed on the slides.

## 2. Create your first API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "hello world"
```
1. Once you are connected to the server
2. Create a new file called `simple_api.py` using the following command `nano simple_api.py`
3. Copy paste the code above and quit using `ctrl-x`, then press `Y`, followed by `enter`
4. Chose a number between 8000 and 9000, this will be your port number. Launch your API with the following command `uvicorn simple_api:app --host 0.0.0.0  --port <PORT_NUMBER>`. Someone may already have used this port number, in that case just take another one until it works.
5. You can call your api by opening a browser window and visiting: `http://167.99.12.243:<YOUR_PORT_NUMBER>/`. This is the address of your API.

## 3. Create your chatbot
Your API will have two mandatory endpoints:
* `/name` will be a GET endpoint, and its only goal is to return the name of your chatbot.
* `/converse` will be a POST endpoint, its goal is to reply to a running conversation.

This is the blueprint. It has two additional functions (name and converse). The name function returns C3PO, and the converse function returns the last utterance of the conversation. 
```python
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class Conversation(BaseModel):
    utterances: List[str]

app = FastAPI()

@app.get("/")
def index():
    return "hello world"

@app.get("/name")
def name():
    return "C3PO"

@app.post("/converse")
def converse(conversation: Conversation):
    return "You said: " + conversation.utterances[-1]
```
You can copy-paste this code inside your `simple_api.py` file, or you can create a new one. You can then re-run this command `uvicorn simple_api:app --host 0.0.0.0  --port <PORT_NUMBER>`. If you created a new file, please update `simple_api` with the new name of your file.

You can test your current API by visiting `http://167.99.12.243:<PORT_NUMBER>/docs`

## 4. Call your chatbot from Python
Now that we have a "functioning" chatbot, we need a way to interact with it programmatically.
Python has an easy package to do so: `requests`.

Before making our first request to the chatbot, we need to know a few things:
* The URL of the API (its address): in our case `http://167.99.12.243:<YOUR_PORT>`
* The endpoint address: `/name` for the name function
* The method of the endpoint (GET/POST/PUT/DELETE): `/name` expects a `GET` request

We can now call our `/name` function like this:
```python
import requests
r = requests.get("http://167.99.12.243:<YOUR_PORT>/name")
print(r.text)
```

## 5. Integrate an external API into your chatbot
Our chatbot is pretty dumb at the moment! To improve the quality, we will integrate another state-of-the-art chatbot by calling its API. We will use [HuggingFace](https://huggingface.co/) for that.


