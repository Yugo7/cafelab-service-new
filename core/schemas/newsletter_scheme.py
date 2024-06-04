from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class NewsletterPost(BaseModel):
    _id: ObjectIdField()
    email: str


class NewsletterResponseGet(BaseModel):
    """
    UserLoginResponseGet schema fastapi
    """
    msg: str
    data: object
