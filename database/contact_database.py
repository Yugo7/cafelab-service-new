import datetime

import core.models as model
from mongoengine import connect
import json

import internal


CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"


def add_contact(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.contact_model.Contact(
        first_name=values.first_name,
        last_name=values.last_name,
        phone=values.phone,
        email=values.email,
        description=values.description,

    ).save()
    return str(response.auto_id_0)


def delete_contact(contact_id):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.contact_model.Contact.objects(_id=contact_id).delete()
    if response:
        return True
    else:
        return False


def return_all_contact():
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.contact_model.Contact.objects().to_json()
    response = json.loads(response)
    return response
