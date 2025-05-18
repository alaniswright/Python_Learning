from pydantic import BaseModel, EmailStr, conint
from typing import Optional, Annotated
from pydantic.types import conint
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# Base model for shared fields
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# Input model for creating a post
class PostCreate(PostBase):
    pass

# Output model for returning posts (includes nested owner info)
class Post(PostBase):
    id: int
    created_at: datetime
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


# Response model
class PostResponse(Post):

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0,le=1)
