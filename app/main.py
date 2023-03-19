from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_val
# from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    predicted_soil_moisture: str


@app.get("/")
def home():
    return {"check": "OK", "model_version": "hi"}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    moisture_value = predict_val(payload.text)
    return {"predicted_soil_moisture": moisture_value}


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}