from fastapi import FastAPI
import random


app=FastAPI()


names=["Arun","Priya","Ragul","Divya"]
@app.get("/student")
def get_student():
    name=random.choice(names)
    age=random.randint(18,25)
    return{"name":name,
            "age":age
            }