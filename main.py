from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": f"User '{user.name}' created", "user": user}

@app.get("/users")
def read_users():
    return {"users": users}

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str):
    users[user_id] = name
    return {"message": f"User '{user_id}' updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = users.pop(user_id)
    return {"message": f"User '{user}' deleted"}