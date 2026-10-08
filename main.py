from fastapi import FastAPI

app=FastAPI()
@app.get("/weather")
def get_weather(city:str,temperature:int):
    return{"city":city,
    "temperature":temperature,
    "message":"Weather information received"h }

