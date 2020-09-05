from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def home():
    return {"message":"Hello Mollie"}


@app.post("/predict")
def predict():
    return {"message":"ano"}
