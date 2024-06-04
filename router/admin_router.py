import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
router = APIRouter()


@router.get("/login/{email}/{password}",
            response_model=schema.admin_scheme.UserLoginResponseGet,
            summary="Return login",
            response_description="Return login",
            description="Return login",
            operation_id="ReturnLoginByEmailPassword")
async def service(email: str, password: str):
    """
    return Login User by Email and Password
    :param email:
    :param password:
    :return:
    """
    response = database.admin_database.return_admin_login(email, password)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Email or password incorrect",
            type="error",
            data="Email or password incorrect"
        )))


@router.post("",
             response_model=schema.admin_scheme.UserLoginResponseGet,
             summary="Create admin",
             response_description="Create admin",
             description="Create admin",
             operation_id="CreateAdmin")
async def service(values: schema.admin_scheme.AdminPost):
    response = database.admin_database.add_admin_user(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))


@router.put("/password",
            response_model=schema.admin_scheme.UserLoginResponseGet,
            summary="Edit password admin",
            response_description="Edit password admin",
            description="Edit password admin",
            operation_id="EditPasswordAdmin")
async def service(email: str, password: str):
    response = database.admin_database.edit_password_admin_by_email(email, password)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))


@router.get("/all",
            response_model=schema.admin_scheme.UserLoginResponseGet,
            summary="Return all admins",
            response_description="Return all admins",
            description="Return all admins",
            operation_id="ReturnAllAdmins")
async def service():
    """
    Return all admins
    :return:
    """
    response = database.admin_database.return_all_admins()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="Admin not found",
            type="error",
            data="Admin not found"
        )))



@router.delete("",
               response_model=schema.admin_scheme.UserLoginResponseGet,
               summary="Delete admin",
               response_description="Delete admin",
               description="Delete admin",
               operation_id="DeleteAdminById")
async def service(admin_id: str):
    response = database.admin_database.delete_admin(admin_id)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Email or password incorrect",
            type="error",
            data="Email or password incorrect"
        )))