import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
router = APIRouter()


@router.post("",
             response_model=schema.orders_scheme.OrdersPostResponse,
             summary="Create Order",
             response_description="Create Order",
             description="Create Order",
             operation_id="CreateOrder")
async def service(values: schema.orders_scheme.OrdersPost):
    response = database.orders_database.add_payment(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Order not created",
            type="error",
            data="Order not created"
        )))


@router.get("/all",
            response_model=schema.orders_scheme.OrdersPostResponse,
            summary="Return all Order",
            response_description="Return all Order",
            description="Return all Order",
            operation_id="ReturnAllOrder")
async def service():
    response = database.orders_database.return_all_payments()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="Order not found",
            type="error",
            data="Order not found"
        )))


@router.delete("/{id_order}",
               response_model=schema.orders_scheme.OrdersPostResponse,
               summary="Delete Order",
               response_description="Delete Order",
               description="Delete Order",
               operation_id="DeleteOrder")
async def service(id_order):
    response = database.orders_database.delete_payment(id_order)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Order not deleted",
            type="error",
            data="Order not deleted"
        )))


@router.put("",
            response_model=schema.orders_scheme.OrdersPostResponse,
            summary="Update Order",
            response_description="Update Order",
            description="Update Order",
            operation_id="UpdateOrder")
async def service(values: schema.orders_scheme.OrdersPut):
    response = database.orders_database.update_payment(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Order not updated",
            type="error",
            data="Order not updated"
        )))