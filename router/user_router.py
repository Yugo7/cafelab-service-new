import json
from starlette import status
import core.schemas.user_scheme as schema
import database
from fastapi import APIRouter, HTTPException, Response
import requests
router = APIRouter()


@router.post("",
             response_model=schema.UserPostResponse,
             summary="Create User",
             response_description="Create User",
             description="Create User",
             operation_id="CreateUser")
async def service(values: schema.UserPost):
    check_user_exist = database.user_database.return_user_by_email_check(values.email)
    if check_user_exist is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User already exist",
            type="error",
            data="User already exist"
        )))
    response = database.user_database.add_user(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not created",
            type="error",
            data="User not created"
        )))


@router.put("",
            response_model=schema.UserGetResponse,
            summary="Update User",
            response_description="Update User",
            description="Update User",
            operation_id="UpdateUser")
async def service(values: schema.UserPut):
    response = database.user_database.update_user(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not updated",
            type="error",
            data="User not updated"
        )))


@router.get("/by-email",
            response_model=schema.UserGetResponse,
            summary="Return User by email",
            response_description="Return User by email",
            description="Return User by email",
            operation_id="ReturnUserByEmail")
async def service(email_user, res: Response):
    response = database.user_database.return_user_by_email(email_user)
    if response is not None:
        res.set_cookie(key="id_account", value=response["_id"]["$oid"])
        print(response["_id"]["$oid"])
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.get("/all",
            response_model=schema.UserGetResponse,
            summary="Return all Users",
            response_description="Return all Users",
            description="Return all Users",
            operation_id="ReturnAllUsers")
async def service():
    response = database.user_database.return_all_user()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.get("/login/{email}/{password}",
            response_model=schema.UserGetResponse,
            summary="Return login",
            response_description="Return login",
            description="Return login",
            operation_id="ReturnUserLoginByEmailPassword")
async def service(email: str, password: str, res: Response):
    response = database.user_database.return_user_login(email, password)
    res.set_cookie(key="id_account", value=response["_id"]["$oid"])
    print(response["_id"]["$oid"])
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Email or password incorrect",
            type="error",
            data="Email or password incorrect"
        )))


@router.delete("/{id_user}",
               response_model=schema.UserGetResponse,
               summary="Delete User",
               response_description="Delete User",
               description="Delete User",
               operation_id="DeleteUser")
async def service(id_user: str):
    response = database.user_database.delete_user(id_user)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not deleted",
            type="error",
            data="User not deleted"
        )))


@router.patch("/update/password/account/{id_user}/{password}",
              response_model=schema.UserGetResponse,
              summary="Update password",
              response_description="Update password",
              description="Update password",
              operation_id="UpdatePassword")
async def service(id_user: str, password: str):
    response = database.user_database.update_password_account(id_user, password)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Password not updated",
            type="error",
            data="Password not updated"
        )))
    

