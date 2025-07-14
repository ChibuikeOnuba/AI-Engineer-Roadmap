from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return [
    {
        "type": "command",
        "details": {
            "key": "python.execInTerminal"
        }
    }
]