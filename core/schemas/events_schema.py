from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class EventsPost(BaseModel):
    _id: ObjectIdField()
    title: str
    date: str
    description: str
    picture: str


class EventsPut(BaseModel):
    event_id: str
    title: str
    date: str
    description: str
    picture: str


class EventsResponse(BaseModel):
    """
    UserLoginResponseGet schema fastapi
    """
    msg: str
    data: object
