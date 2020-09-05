from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


app = FastAPI()



@app.get("/")
def home():
    return {"message":"Hello Mollie"}


@app.post("/predict")
def predict():
    return {"message":"ano"}
