import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
router = APIRouter()


@router.post("",
             response_model=schema.newsletter_scheme.NewsletterResponseGet,
             summary="Create newsletter",
             response_description="Create newsletter",
             description="Create newsletter",
             operation_id="CreateNewsletter")
async def service(values: schema.newsletter_scheme.NewsletterPost):
    response = database.newsletter_database.add_newsletter_email(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Newsletter not created",
            type="error",
            data="Newsletter not created"
        )))


@router.get("/all",
             response_model=schema.newsletter_scheme.NewsletterResponseGet,
             summary="Return all newsletter",
             response_description="Return all newsletter",
             description="Return all newsletter",
             operation_id="ReturnAllNewsletter")
async def service():
    response = database.newsletter_database.return_all_newsletter()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=json.dumps(dict(
            msg="Newsletter not found",
            type="error",
            data="Newsletter not found"
        )))