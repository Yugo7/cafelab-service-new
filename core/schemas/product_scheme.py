from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class ProductPost(BaseModel):
    _id: ObjectIdField()
    name: str = Field(alias="name", default="")
    description: str = Field(alias="description", default="")
    origin: str = Field(alias="origin", default="")
    grain: str = Field(alias="grain", default="")
    price: float = Field(alias="price", default=0.0)
    picture: str = Field(alias="picture", default="")
    section: str = Field(alias="section", default="")


class ProductResponse(BaseModel):
    msg: str
    data: object


class ProductPut(BaseModel):
    product_id: str
    name: Optional[str] = Field(alias="name", default="Optional_name_value")
    description: Optional[str] = Field(alias="description", default="Optional_description_value")
    origin: Optional[str] = Field(alias="origin", default="Optional_origin_value")
    grain: Optional[str] = Field(alias="grain", default="Optional_grain_value")
    price: Optional[float] = Field(alias="price", default=0.0)
    picture: Optional[str] = Field(alias="picture", default="Optional_picture_value")
    section: Optional[str] = Field(alias="section", default="Optional_section_value")

