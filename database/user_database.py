import datetime

import core.models.user_model as model
import core.schemas
from mongoengine import connect
import json
import stripe

import internal

CONNECTION = "mongodb+srv://blancog04:gabiman123@coffelab-db.ljkszos.mongodb.net/?retryWrites=true&w=majority&appName=coffelab-db"
stripe.api_key = 'sk_test_51PEHtQRuE32NAoOjrVMXtKwv3Qwt7Mw0jV7fwWFTRUqUma2i3NVdBGY3ygRuPrWdaIb0mNAm4sgd8BSfYGsIz8gf00ZOL7Px6I'


def add_user(user_data):
    db_uri = CONNECTION
    connect(host=db_uri)
    stripe_id = stripe.Customer.create(email=user_data.email)
    new_user = model.User(
        name=user_data.name,
        profile_image=user_data.profile_image,
        email=user_data.email,
        password=internal.crypt.encrypt(user_data.password) if len(user_data.password) > 0 else "",
        address=user_data.address,
        zip_code=user_data.zip_code,
        nif=user_data.nif,
        date_birth=user_data.date_birth,
        is_subscribed=False,
        stripe_id=str(stripe_id.id),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Save the new user document to the database
    new_user.save()
    return str(new_user.auto_id_0)


def update_user(user_data):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.User.objects(_id=user_data.user_id).update_one(
        name=user_data.name,
        profile_image=user_data.profile_image,
        email=user_data.email,
        address=user_data.address,
        zip_code=user_data.zip_code,
        nif=user_data.nif,
        date_birth=user_data.date_birth,
        updated_at=datetime.datetime.now()
    )
    if response == 1:
        return True
    else:
        return False


def return_user_by_email(email):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects(email=email).first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None

    return response_database


def return_user_by_email_check(email):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects(email=email).first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None

    return response_database


def return_user_by_id(id_user):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects(_id=id_user).exclude("password").first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None

    return response_database


def return_all_user():
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects().exclude("password").to_json()
    response_database = json.loads(response_database)
    return response_database


def return_user_login(email, password):
    db_uri = CONNECTION
    connect(host=db_uri)
    get_user_by_email = return_user_by_email(email)
    if get_user_by_email is not None:
        get_password_encrypted = internal.crypt.decrypt(get_user_by_email["password"].encode("utf-8"))
        response_database = model.User.objects(email=email).exclude("password").first()
        response_database = json.loads(response_database.to_json()) if response_database is not None else None
        if response_database["email"] == email and get_password_encrypted == password:
            return response_database


def delete_user(id_user):
    db_uri = CONNECTION
    connect(host=db_uri)
    response = model.User.objects(_id=id_user).delete()
    return True if response == 1 else False


def update_password_account(id_user, password):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects(_id=id_user).update_one(
        password=internal.crypt.encrypt(password)
    )
    return response_database


def update_is_subscribed_by_email(email, trueOrFalse):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects(email=email).update_one(
        is_subscribed=trueOrFalse
    )
    return response_database


def update_subscription_id_by_email(email, data):
    db_uri = CONNECTION
    connect(host=db_uri)
    response_database = model.User.objects(email=email).update_one(
        subscription_id=data
    )
    return response_database

