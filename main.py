# main.py
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(data: TextInput):
    pred = model.predict([data.text])[0]
    return {"label": "POSITIVE" if pred == 1 else "NEGATIVE"}
