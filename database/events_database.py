import datetime

import core.models as model
from mongoengine import connect
import json

import internal


CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"


def add_events(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.events_model.Events(
        title=values.title,
        date=values.date,
        description=values.description,
        picture=values.picture
    ).save()
    return str(response.auto_id_0)


def delete_event(event_id):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.events_model.Events.objects(_id=event_id).delete()
    if response:
        return True
    else:
        return False


def return_all_events():
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.events_model.Events.objects().to_json()
    response = json.loads(response)
    return response


def return_events_by_id(event_id):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.events_model.Events.objects(_id=event_id).first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None
    return response_database


def update_product_by_id(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.events_model.Events.objects(_id=values.event_id).update_one(
        title=values.title,
        date=values.date,
        description=values.description,
        picture=values.picture
    )
    if response == 1:
        return True
    else:
        return False
