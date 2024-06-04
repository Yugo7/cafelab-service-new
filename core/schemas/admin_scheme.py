from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class AdminPost(BaseModel):
    _id: ObjectIdField()
    name: str
    email: str
    password: str


class UserLoginResponseGet(BaseModel):
    """
    UserLoginResponseGet schema fastapi
    """
    msg: str
    data: object
