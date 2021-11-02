# computing101

## Connect to our server

1. Connect to the server using: https://sshwifty.herokuapp.com/
2. Your username is the concatenation of the letter "u" and your student ID: u<STUDENT_ID>
3. The password will be on the slides

## Create your first API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
1. Once you are connected to the server
2. Create a new file called `simple_api.py` using the following command `nano simple_api.py`
3. Copy paste the code above and quit using `ctrl-x`, then press `Y`, followed by `enter`
4. Chose a number between 8000 and 9000, this will be your port number. Launch your API with the following command `uvicorn simple_api:app --host 0.0.0.0  --port <PORT_NUMBER>`. Someone may already have used this port number, in that case just take another one until it works.
5. You can call your api by opening a browser window and visiting: `http://167.99.12.243:<YOUR_PORT_NUMBER>/`
6. Kill the process with `ctrl-c` and replace the return value of `read_root()` with your name.

