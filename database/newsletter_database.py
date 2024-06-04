import datetime

import core.models as model
from mongoengine import connect
import json

import internal


CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"


def add_newsletter_email(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.newsletter_model.Newsletter(
        email=values.email
    ).save()
    return str(response.auto_id_0)


def return_all_newsletter():
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.newsletter_model.Newsletter.objects().to_json()
    response = json.loads(response)
    return response