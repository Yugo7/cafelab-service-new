from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class ContactPost(BaseModel):
    _id: ObjectIdField()
    first_name: str
    last_name: str
    phone: str
    email: str
    description: str


class ContactGetResponseGet(BaseModel):
    """
    UserLoginResponseGet schema fastapi
    """
    msg: str
    data: object

