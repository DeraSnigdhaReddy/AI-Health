from fastapi import FastAPI 
from pydantic import BaseModel
import google.generativeai as genai
from transformers import pipeline
from llm_response import generate_health_info,analyse_sentiment

app = FastAPI()

class Patientdata(BaseModel):
    Name: str
    Age: int
    Weight: float
    History: str
    Symptoms: str

@app.post("/predict")
def prediction(data:Patientdata):
    datas=data.dict()
    generated_res = generate_health_info(datas)

    sentiment_res = analyse_sentiment(data.History +" "+data.Symptoms )

    return {
        "Ai response" : generated_res,
        "conditional Status": sentiment_res
    }



