import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
router = APIRouter()


@router.post("",
             response_model=schema.product_scheme.ProductResponse,
             summary="Create Product",
             response_description="Create Product",
             description="Create Product",
             operation_id="CreateProduct")
async def service(values: schema.product_scheme.ProductPost):
    response = database.product_database.create_product(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not created",
            type="error",
            data="Product not created"
        )))


@router.put("",
            response_model=schema.product_scheme.ProductResponse,
            summary="Update Product",
            response_description="Update Product",
            description="Update Product",
            operation_id="UpdateProduct")
async def service(product_values: schema.product_scheme.ProductPut):
    response = database.product_database.update_product_by_id(product_values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not updated",
            type="error",
            data="Product not updated"
        )))


@router.get("/all",
            response_model=schema.product_scheme.ProductResponse,
            summary="Return all Products",
            response_description="Return all Products",
            description="Return all Products",
            operation_id="ReturnAllProducts")
async def service():
    response = database.product_database.get_all_products()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Products not found",
            type="error",
            data="Products not found"
        )))


@router.delete("/{id_product}",
               response_model=schema.product_scheme.ProductResponse,
               summary="Delete Product",
               response_description="Delete Product",
               description="Delete Product",
               operation_id="DeleteProduct")
async def service(id_product: str):
    response = database.product_database.delete_product_by_id(id_product)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not deleted",
            type="error",
            data="Product not deleted"
        )))


@router.get("/{id_product}",
            response_model=schema.product_scheme.ProductResponse,
            summary="Return Products by id",
            response_description="Return Products by id",
            description="Return Products by id",
            operation_id="ReturnProductById")
async def service(id_product):
    response = database.product_database.return_product_by_id(id_product)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not found",
            type="error",
            data="Product not found"
        )))