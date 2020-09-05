from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from anonimizer import Anonimizer

app = FastAPI()

class Input(BaseModel):
    """Data model for post request form"""

    customer: str
    payment_type: str
    merchant: str
    category: str
    amount: str
    Country_account: str

@app.get("/")
def home():
    return {"message":"Hello Mollie"}


@app.post("/predict")
def predict(params: Input):
    print(params)
    return {"message":"ano"}
