import datetime

import core.models as model
from mongoengine import connect
import json

import internal


CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"


def add_admin_user(values):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.admin_model.Admin(
        name=values.name,
        email=values.email,
        password=internal.crypt.encrypt(values.password) if len(values.password) > 0 else "",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    ).save()
    return str(response.auto_id_0)


def return_all_admins():
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.admin_model.Admin.objects().exclude("password").to_json()
    response = json.loads(response)
    return response


def edit_password_admin_by_email(email, password_value):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.admin_model.Admin.objects(email=email).update_one(
        password=internal.crypt.encrypt(password_value) if len(password_value) > 0 else "",
        updated_at=datetime.datetime.now()
    )
    if response == 1:
        return True
    else:
        return False


def return_admin_by_email(email):
    """
    Return user in database by email
    :return: json
    """
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.admin_model.Admin.objects(email=email).first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None
    return response_database


def return_admin_login(email, password):
    """
    Return Login by email and password
    :param email:
    :param password:
    :return: json
    """
    db_uri = CONNECTION
    connect(host=db_uri)
    get_user_by_email = return_admin_by_email(email)
    if get_user_by_email is not None:
        get_password_encrypted = internal.crypt.decrypt(get_user_by_email["password"].encode("utf-8"))
        response_database = model.admin_model.Admin.objects(email=email).exclude("password").first()
        response_database = json.loads(response_database.to_json()) if response_database is not None else None
        if response_database["email"] == email and get_password_encrypted == password:
            return response_database


def delete_admin(admin_id):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.admin_model.Admin.objects(_id=admin_id).delete()
    if response:
        return True
    else:
        return False
