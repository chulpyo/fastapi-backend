from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4

app = FastAPI()

# 사용자 목록을 딕셔너리로 관리
users = {}

class User(BaseModel):
    id: str
    name: str
    age: int

class UserCreate(BaseModel):
    name: str
    age: int

# 사용자 전체 조회
@app.get("/users", response_model=List[User])
def read_users():
    return [user for key, user in users.items()]

# 사용자 생성
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    user_id = str(uuid4())
    new_user = User(id=user_id, name=user.name, age=user.age)
    users[user_id] = new_user
    return new_user

# 사용자 조회
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: str):
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 사용자 수정
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, name: Optional[str] = None, age: Optional[int] = None):
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if name:
        user.name = name
    if age:
        user.age = age
    users[user_id] = user
    return user

# 사용자 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    user = users.pop(user_id, None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User '{user.name}' deleted"}