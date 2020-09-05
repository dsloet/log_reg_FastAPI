from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def home():
    return {"message":"Hello Mollie"}


@app.post("/predict")
def predict():
    return {"message":"ano"}
