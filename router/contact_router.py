import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
router = APIRouter()


@router.post("",
             response_model=schema.contact_scheme.ContactGetResponseGet,
             summary="Create contact",
             response_description="Create contact",
             description="Create contact",
             operation_id="CreateContact")
async def service(values: schema.contact_scheme.ContactPost):
    response = database.contact_database.add_contact(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Contact not created",
            type="error",
            data="Contact not created"
        )))


@router.get("/all",
            response_model=schema.contact_scheme.ContactGetResponseGet,
            summary="Return all contact",
            response_description="Return all contact",
            description="Return all contact",
            operation_id="ReturnAllContact")
async def service():
    response = database.contact_database.return_all_contact()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="Contact not found",
            type="error",
            data="Contact not found"
        )))


@router.delete("",
               response_model=schema.contact_scheme.ContactGetResponseGet,
               summary="Delete contact",
               response_description="Delete contact",
               description="Delete contact",
               operation_id="DeleteContactById")
async def service(contact_id: str):
    response = database.contact_database.delete_contact(contact_id)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Contact not deleted",
            type="error",
            data="Contact not deleted"
        )))
