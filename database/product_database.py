import datetime

import core.models as model
from mongoengine import connect
import json

import internal


CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"


def create_product(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.product_model.Product(
        name=values.name,
        description=values.description,
        origin=values.origin,
        grain=values.grain,
        price=values.price,
        picture=values.picture,
        section=values.section,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    ).save()
    return str(response.auto_id_0)


def update_product_by_id(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.product_model.Product.objects(_id=values.product_id).update_one(
        name=values.name,
        description=values.description,
        origin=values.origin,
        grain=values.grain,
        price=values.price,
        picture=values.picture,
        section=values.section,
        updated_at=datetime.datetime.now()
    )
    if response == 1:
        return True
    else:
        return False


def get_all_products():
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.product_model.Product.objects().to_json()
    response = json.loads(response)
    return response


def return_product_by_id(product_id):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.product_model.Product.objects(_id=product_id).first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None
    return response_database


def delete_product_by_id(product_id):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.product_model.Product.objects(_id=product_id).delete()
    if response_database:
        return True
    else:
        return False
