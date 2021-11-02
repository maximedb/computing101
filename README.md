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

## 3. Develop your chatbot


