from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

from anonimizer import Anonimizer

ano = Anonimizer()
ano.load_model("ano.pickle")
print(ano.meta_list)

app = FastAPI()
origins = ["http://localhost:8081"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.post("/predict")
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
    # prediction = loaded_model.predict([[ 1.29312543e+03, -1.21054113e+02,  2.56682337e+01,
    #      2.36900295e+00,  2.56859542e-01,  1.57038999e+00]])
    if prediction == 1:
        return "prediction is Fraud"
    else:
        return "prediction is non fraud"
