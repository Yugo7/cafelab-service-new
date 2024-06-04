from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class OrdersPostStripe(BaseModel):
    _id: ObjectIdField()
    user_id: Optional[str]
    address: str
    zip_code: str
    product_id: list
    status: Optional[str]
    amount: float
    currency: str


class OrdersPost(BaseModel):
    _id: ObjectIdField()
    user_id: str
    address: str
    product_id: list
    status: str
    zip_code: str
    amount: float


class OrdersPostResponse(BaseModel):
    msg: str
    data: object


class OrdersGetResponse(BaseModel):
    msg: str
    data: object


class OrdersPut(BaseModel):
    id_payment: str
    user_id: Optional[str] = Field(default="default_user_id", alias="user_id")
    address: Optional[str] = Field(default="default_address", alias="address")
    product_id: Optional[list] = Field(default=["default_product_id"], alias="product_id")
    status: Optional[str] = Field(default="default_status", alias="status")
    amount: Optional[float] = Field(default=0.0, alias="amount")
    zip_code: Optional[str] = Field(default="zip_code", alias="zip_code")


class CreateSubscriptionRequest(BaseModel):
    email: str
    payment_method_id: str
    price_id: str


class CancelSubscriptionRequest(BaseModel):
    email: str
    subscription_id: str

