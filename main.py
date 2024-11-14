from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional, List
from uuid import uuid4

app = FastAPI()

# 사용자 모델 정의
class User(BaseModel):
    id: str
    name: str
    age: int

class UserCreate(BaseModel):
    name: str
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

USER_NOT_FOUND = "User not found"

users: Dict[str, "User"] = {}

# 사용자 전체 조회
@app.get("/users", response_model=List[User])
def read_users():
    return list(users.values())

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
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return user

# 사용자 수정
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, user_update: UserUpdate):
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    if user_update.name:
        user.name = user_update.name
    if user_update.age:
        user.age = user_update.age
    return user

# 사용자 삭제
@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: str):
    user = users.pop(user_id, None)
    if user is None:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return user