from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class UserPost(BaseModel):
    _id: ObjectIdField()
    name: str = Field(default="default_value_1", alias="name")
    profile_image: Optional[str] = Field(default="", alias="profile_image")
    email: str = Field(default="example@gmail.com", alias="email")
    password: str = Field(alias="password")
    address: str = Field(default="", alias="address")
    zip_code: str = Field(default="",alias="zip_code")
    nif: str = Field(default="", alias="nif")
    date_birth: str = Field(default="", alias="date_birth")


class UserPostResponse(BaseModel):
    msg: str
    data: object


class UserGetResponse(BaseModel):
    msg: str
    data: object


class UserPut(BaseModel):
    user_id: str
    name: Optional[str] = Field(default="default_value_1", alias="name")
    profile_image: Optional[str] = Field(default="default_value_2", alias="profile_image")
    email: Optional[str] = Field(default="default_value_3", alias="email")
    address: Optional[str] = Field(default="default_value_5", alias="address")
    zip_code: str = Field(default="",alias="zip_code")
    nif: Optional[str] = Field(default="default_value_6", alias="nif")
    date_birth: Optional[str] = Field(default="default_value_7", alias="date_birth")
