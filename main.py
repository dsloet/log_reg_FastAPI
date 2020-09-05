from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

from anonimizer import Anonimizer

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.

ano = Anonimizer()
ano.load_model("ano.pickle")
print(ano.meta_list)

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
    return {"message":"Hello TutLinks.com"}


@app.get("/predict")
def predict(params: Input):
    print(params)
    filename = 'log_reg.pickle'
    loaded_model = pickle.load(open(filename, 'rb'))
    data = [[params.customer, params.payment_type, params.merchant,
             params.category, params.amount, params.Country_account]]
    print(data)
    data = pd.DataFrame(data, columns=['customer', 'payment_type', 'merchant', 'category', 'amount',
                                       'Country_account'])

    print(data.head())
    data = ano.transform(data)
    print("transformed data")
    print(data)



    prediction = loaded_model.predict(data)

    if prediction == 1:
        return {"message":"prediction is Fraud"}
    else:
        return {"message":"prediction is non fraud"}
