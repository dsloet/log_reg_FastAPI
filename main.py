from fastapi import FastAPI

@app.get("/")
def home():
    return {"message":"Hello Mollie"}


@app.post("/predict")
def predict(params: Input):
    return {"message":"prediction is non fraud"}
