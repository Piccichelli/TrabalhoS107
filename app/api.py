from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Hello World!'}

@app.get("/{name}")
def welcome(name: str):
    return {'message': f'Hello {name}'}