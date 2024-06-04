from fastapi import APIRouter, File, UploadFile, HTTPException
from mongoengine import connect, Document, StringField, DateTimeField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import requests
import base64
import core.schemas as schema

router = APIRouter()

IMGBB_API_KEY = 'e8f0199158434cb961ebcee9356c27ca'
IMGBB_UPLOAD_URL = 'https://api.imgbb.com/1/upload'


@router.post("",
             response_model=schema.image_scheme.ImageResponse,
             summary="Upload image",
             response_description="Upload image",
             description="Upload image",
             operation_id="UploadImage")
async def service(file: UploadFile = File(...)):
    try:
        # Read the file and encode it to base64
        image_data = await file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')

        # Prepare the payload for ImgBB API
        payload = {
            'key': IMGBB_API_KEY,
            'image': base64_image,
        }

        # Make the POST request to the ImgBB API
        response = requests.post(IMGBB_UPLOAD_URL, data=payload)

        # Check the response from ImgBB API
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Image upload failed")

        response_data = response.json()
        image_url = response_data['data']['url']

        return {"url": image_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))