from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

from anonimizer import Anonimizer


app = FastAPI()

ano = Anonimizer()
ano.load_model("ano.pickle")
print(ano.meta_list)

@app.get("/")
def home():
    return {"message":"Hello Mollie"}


@app.post("/predict")
def predict():
    return {"message":ano.meta_list}
