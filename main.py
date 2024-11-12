from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

# 사용자 목록 저장
users = []

# 사용자 데이터 모델 정의
class User(BaseModel):
    id: str
    name: str
    age: int

class UserCreate(BaseModel):
    name: str
    age: int

# 사용자 생성 (id 자동 할당)
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    new_user = User(id=str(uuid4()), name=user.name, age=user.age)
    users.append(new_user)
    return new_user

# 사용자 전체 조회
@app.get("/users", response_model=List[User])
def read_users():
    return users

# 사용자 ID로 조회
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: str):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 사용자 정보 수정
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, name: Optional[str] = None, age: Optional[int] = None):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if name:
        user.name = name
    if age:
        user.age = age
    return user

# 사용자 삭제
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    global users
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users = [u for u in users if u.id != user_id]
    return {"message": f"User '{user.name}' deleted"}