# Computing101

The goal of the session is to introduce you to the world of servers and APIs. At the end of the session, you will have built your own chatbot and will host it on a live server.

## Takeaways
1. Discover the world of servers
2. Learn about APIs
3. Learn about [TextGain](https://textgain.com)

## 1. Connect to the server

1. Connect to the server using: https://sshwifty.herokuapp.com/
2. Your username is written on the piece of paper you received.
3. Your password is written on the piece of paper you received.

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
Your API will expose two mandatory endpoints:
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

## 4. Call an API from Python
How do you interact with an (HTTP) API from Python? We made available an Eliza API that you can interact with. Eliza is one of the first chatbot released in the computational linguistics community in 1966, click [here](https://github.com/wadetb/eliza/blob/master/p36-weizenabaum.pdf) for me info. 

This chatbot is available at: `http://167.99.12.243:1000`. You can visit the documentation here: http://167.99.12.243:1000/docs
It exposes two endpoints: `/name` and `/converse` 

You can easily interact with it using the `requests` package from Python.

We can now call the `/name` function like this:
```python
import requests
r = requests.get("http://167.99.12.243:1000/name")
print(r.json())
```
`/name` expects a GET request so we use `requests.get(url)` 
Calling the `/converse` endpoint is a little different as it expects a POST request with some data:
```python
import requests
r = requests.post("http://167.99.12.243:1000/converse", json={"utterances": ["how are you doing?"]})
print(r.json())
```
You can interact with Eliza using this online tool: http://167.99.12.243:2000

## 5. Excercise 1: integrate an external API into your chatbot
Our chatbot is pretty dumb at the moment! Can we make it better by integrating 3rd party APIs?

There are several models we can integrate by using their API:
* Eliza (easy): you can find a running API for Eliza at http://167.99.12.243:1000/docs. You can simply integrate the example from the previous section and replace `["hi"]` with conversation.utterances
* Blender (hard/expert): integrate a Blender model into your chatbot: https://huggingface.co/facebook/blenderbot-1B-distill. Click on "deploy" and "accelerated inference".

```python
import requests
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
    r = requests.post("http://0.0.0.0:1000/converse", json={"utterances": conversation.utterances})
    return r.json()
```
 
## 6. Exercise 2: detect non-supported languages
Our model only speaks English. Can you integrate the language identification API offered by [TextGain](https://www.textgain.com/) to detect if a new utterance is another language than English? If it is not in English, answer that you do not speak the identified language.
[API documentation for Language Identification](https://devops.textgain.com/#tag/Identification/paths/~1language/get).

```python
import requests
r = requests.get("https://api.textgain.com/language", params={"q": "Hi there!", "key": "<ASK_FOR_THE_KEY>"})
print(r.json())
```

## 7. End
Well done you connected to a live server and create your first chatbot. The server will be shutdown this evening, so copy-paste the stuff you want to keep.

