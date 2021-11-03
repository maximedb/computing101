# Computing101

The goal of the session is to introduce you to the world of servers and APIs. At the end of the session, you will have built your own chatbot and will host it on a live server.

## Takeaways
1. Discover the world of servers
2. Learn about APIs
3. Learn about [TextGain](https://textgain.com)

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
4. Check the port number assigned to you (paper you received) and launch your API with the following command `uvicorn simple_api:app --host 0.0.0.0  --port <PORT_NUMBER>`.
5. You can call your api by opening a browser window and visiting: `http://167.99.12.243:<YOUR_PORT_NUMBER>/`. This is the address of your API.

## 3. Create your chatbot
Your API will have two mandatory endpoints:
* `/name` will be a GET endpoint, and its only goal is to return the name of your chatbot.
* `/converse` will be a POST endpoint, its goal is to reply to a running conversation.

Your API now has two additional functions: name and converse. Users can call the name function to get the name of your bot, they can interact with your bot by using the converse function. At the moment, the converse function only copies the last utterance and appends *you said:* to it. 
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
    if len(conversation.utterances) > 0:
        return "You said: " + conversation.utterances[-1]
    else:
        return "Hi!"
```
You can copy-paste this code inside your `simple_api.py` file, or you can create a new one. You can then re-run this command `uvicorn simple_api:app --host 0.0.0.0  --port <PORT_NUMBER>`. If you created a new file, please update `simple_api` with the new name of your file.

You can test your current API by visiting `http://167.99.12.243:<PORT_NUMBER>/docs`.
You can also interact visually with your chatbot using Streamlit: http://167.99.12.243:2000/

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
r = requests.get("http://167.99.12.243:1000/name")
print(r.json())
```
Calling the `/converse` endpoint is a little different:
```python
import requests
r = requests.post("http://167.99.12.243:1000/converse", json={"utterances": ["hi"]})
print(r.json())
```

## 5. Integrate an external API into your chatbot
Our chatbot is pretty dumb at the moment! 

There are several models we can integrate by using their API:
* Eliza (easy): you can find a running API for Eliza at http://167.99.12.243:1000/docs
* Blender (moderate/hard): integrate a Blender model into your chatbot: https://huggingface.co/facebook/blenderbot-1B-distill
 
## 6. Execrice
Our model only speaks English. Can you integrate the language identification API offered by [TextGain](https://www.textgain.com/) to detect if a new utterance is another language than English? If it is not in English, answer that you do not speak the identified language.
[API documentation for Language Identification](https://devops.textgain.com/#tag/Identification/paths/~1language/get).

