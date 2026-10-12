from fastapi import FastAPI
import random

app = FastAPI()

names = ["Priya", "Rithan", "Iniya", "Saravana"]

addresses = [
    {"door_no": "12", "street": "Gandhi Road", "city": "Salem"},
    {"door_no": "45", "street": "Nehru Street", "city": "Chennai"},
    {"door_no": "28", "street": "Anna Nagar Main Road", "city": "Coimbatore"},
    {"door_no": "7", "street": "Bharathi Street", "city": "Madurai"}
]

@app.get("/student_address")
def get_student_address():
    name = random.choice(names)
    age = random.randint(18, 25)
    address = random.choice(addresses)

    return {
        "name": name,
        "age": age,
        "address": address
    }