from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    is_active: bool
    is_superuser: bool = False

class UserCreate(UserBase):
    username: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: Optional[int] = None

class UserOutDb(BaseModel):
    username: str 
    password: str
    is_active: bool
    
class Users(BaseModel):
    id: int
    username: str 
    password: str
    is_active: bool
    is_superuser: bool

class UsersAll(BaseModel):
    all_users: List[Users]
    
