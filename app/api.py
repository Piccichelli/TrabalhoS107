from fastapi import FastAPI, exceptions
import fastapi

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Hello World!'}

@app.get("/{name}")
def welcome(name: str):
    return {'message': f'Hello {name}'}

@app.post("/calculadora/divisao")
def calculadora(a: float, b: float):
    if b == 0:
        return {"error": "Denominador inválido"}
    return {"resultado": a / b}
