import datetime

import core.models.orders_model as model
from mongoengine import connect
import json

import internal

CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"


def add_payment(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.Orders(
        user_id=values.user_id or "no id provided",
        address=values.address,
        product_id=values.product_id,
        status=values.status,
        amount=values.amount,
        zip_code=values.zip_code,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    response.save()
    return str(response.auto_id_0)


def return_all_payments():
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.Orders.objects().to_json()
    response = json.loads(response)
    return response


def update_payment(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.Orders.objects(_id=values.id_payment).update_one(
        user_id=values.user_id,
        address=values.address,
        product_id=values.product_id,
        status=values.status,
        amount=values.amount,
        zip_code=values.zip_code,
        updated_at=datetime.datetime.now(),
    )
    if response == 1:
        return True
    else:
        return False


def delete_payment(id_payment):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.Orders.objects(_id=id_payment).delete()
    return True if response == 1 else False
