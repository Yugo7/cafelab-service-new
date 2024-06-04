from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class ImageResponse(BaseModel):
    url: str