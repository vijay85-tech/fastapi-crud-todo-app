from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str

@app.get("/users", response_model=UserResponse)
def get_user():
    return {"name": "John Doe", "email": "john.doe@example.com"}  # The password will be hidden in the response