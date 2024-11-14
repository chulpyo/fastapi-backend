from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Dict, Optional, List
from uuid import uuid4

# FastAPI 애플리케이션 정의 및 메타데이터 설정
app = FastAPI(
    title="User Management API",
    description="API for managing users, including CRUD operations.",
    version="1.0.0"
)

# 사용자 모델 정의
class User(BaseModel):
    id: str
    name: str
    age: int

class UserCreate(BaseModel):
    # 사용자 생성 입력 모델
    name: str = Field(..., min_length=2, max_length=50, description="The name of the user, between 2 and 50 characters.")
    age: int = Field(..., gt=0, lt=120, description="The age of the user, must be between 1 and 120.")

    # 이름 필드 커스텀 밸리데이션
    @field_validator("name")
    @classmethod
    def name_must_be_alphanumeric(cls, value):
        if not value.isalnum():
            raise ValueError("Name must be alphanumeric.")
        return value

class UserUpdate(BaseModel):
    # 사용자 수정 입력 모델
    name: Optional[str] = Field(None, min_length=2, max_length=50, description="The name of the user, between 2 and 50 characters.")
    age: Optional[int] = Field(None, gt=0, lt=120, description="The age of the user, must be between 1 and 120.")

# 사용자 목록 저장소
USER_NOT_FOUND = "User not found"
users: Dict[str, "User"] = {}

# 사용자 전체 조회
@app.get("/users", response_model=List[User], tags=["Users"], summary="Get All Users", description="Retrieve a list of all users in the system.")
def read_users():
    """
    Retrieve a list of all users.
    """
    return list(users.values())

# 사용자 생성
@app.post("/users", response_model=User, tags=["Users"], summary="Create a User", description="Create a new user with a unique ID.")
def create_user(user: UserCreate):
    """
    Create a new user with a unique ID.
    - Input: UserCreate model (name and age required).
    - Output: The created User object with an ID.
    """
    user_id = str(uuid4())
    new_user = User(id=user_id, name=user.name, age=user.age)
    users[user_id] = new_user
    return new_user

# 사용자 조회
@app.get("/users/{user_id}", response_model=User, tags=["Users"], summary="Get a User", description="Retrieve a user by their unique ID.")
def read_user(user_id: str):
    """
    Retrieve a user by their unique ID.
    - Input: User ID (string).
    - Output: User object if found, 404 error otherwise.
    """
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return user

# 사용자 수정
@app.put("/users/{user_id}", response_model=User, tags=["Users"], summary="Update a User", description="Update a user's information by their unique ID.")
def update_user(user_id: str, user_update: UserUpdate):
    """
    Update a user's information by their unique ID.
    - Input: User ID (string) and optional UserUpdate model.
    - Output: Updated User object, or 404 error if user is not found.
    """
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    if user_update.name:
        user.name = user_update.name
    if user_update.age:
        user.age = user_update.age
    return user

# 사용자 삭제
@app.delete("/users/{user_id}", response_model=User, tags=["Users"], summary="Delete a User", description="Delete a user by their unique ID.")
def delete_user(user_id: str):
    """
    Delete a user by their unique ID.
    - Input: User ID (string).
    - Output: Deleted User object, or 404 error if user is not found.
    """
    user = users.pop(user_id, None)
    if user is None:
        raise HTTPException(status_code=404, detail=USER_NOT_FOUND)
    return user