import json
from starlette import status
import core.schemas as schema
import database
from fastapi import APIRouter, HTTPException
import requests
router = APIRouter()


@router.post("",
             response_model=schema.events_schema.EventsResponse,
             summary="Create event",
             response_description="Create event",
             description="Create event",
             operation_id="CreateEvent")
async def service(values: schema.events_schema.EventsPost):
    response = database.events_database.add_events(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Event not created",
            type="error",
            data="Event not created"
        )))


@router.put("",
            response_model=schema.events_schema.EventsResponse,
            summary="Update event",
            response_description="Update event",
            description="Update event",
            operation_id="UpdateEvent")
async def service(values: schema.events_schema.EventsPut):
    response = database.events_database.update_product_by_id(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Event not updated",
            type="error",
            data="Event not updated"
        )))


@router.get("/all",
            response_model=schema.events_schema.EventsResponse,
            summary="Return all event",
            response_description="Return all event",
            description="Return all event",
            operation_id="ReturnAllEvents")
async def service():
    response = database.events_database.return_all_events()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Event not found",
            type="error",
            data="Event not found"
        )))


@router.delete("/{id_event}",
               response_model=schema.events_schema.EventsResponse,
               summary="Delete event",
               response_description="Delete event",
               description="Delete event",
               operation_id="DeleteEvent")
async def service(id_event: str):
    response = database.events_database.delete_event(id_event)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Event not deleted",
            type="error",
            data="Event not deleted"
        )))


@router.get("/{id_event}",
            response_model=schema.events_schema.EventsResponse,
            summary="Return event by id",
            response_description="Return event by id",
            description="Return event by id",
            operation_id="ReturnEventById")
async def service(id_event):
    response = database.events_database.return_events_by_id(id_event)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Event not found",
            type="error",
            data="Event not found"
        )))