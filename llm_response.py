import google.generativeai as genai 
from transformers import pipeline

genai.configure(api_key="AIzaSyDdgDonnZYmczQ2O2lOyQANccREj203_VU")
model=genai.GenerativeModel("gemini-2.0-flash")

sen_model=pipeline("sentiment-analysis")

def generate_health_info(patient_info:dict):
    prompt = f"""Provide simple health advice for the following patient information:
    Name : {patient_info["Name"]},
    Age : {patient_info["Age"]},
    Weight : {patient_info["Weight"]},
    Medical History : {patient_info["History"]},
    Symptoms : {patient_info["Symptoms"]}

    provide:
    1.A detailed analysis of health pattern,
    2.Possible causes or concerns
    3.Lifestyle or dietary recommendations
    4.Whether a doctors consultation is urgently needed
    5.What lifestyle changes would you recommend.
    """

    response = model.generate_content(prompt)
    # health_advice = response.text.strip()
    return response.text

def analyse_sentiment(text):
    sentiment=sen_model(text)
    return sentiment



