from fastapi import FastAPI
import requests

app = FastAPI()

CALC_URL = "http://calculator:8000/add"

@app.get("/sum")
def sum_proxy(a: int, b: int):
    r = requests.get(CALC_URL, params={"a": a, "b": b})
    return r.json()
