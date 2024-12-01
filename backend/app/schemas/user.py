from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str
    full_name: Optional[str]
    profile_picture: Optional[str]

class UserCreate(UserBase):
    user_id: str  # user_id do người dùng cung cấp
    password: str

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    full_name: Optional[str]
    profile_picture: Optional[str]
    password: Optional[str]

class UserResponse(UserBase):
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True  # Chỉnh sửa để tương thích với Pydantic V2
