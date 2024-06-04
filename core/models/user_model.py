from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class User(Document):
    _id = ObjectIdField()
    name = StringField()
    profile_image = StringField()
    email = StringField()
    password = StringField()
    address = StringField()
    zip_code = StringField()
    nif = StringField()
    date_birth = StringField()
    is_subscribed = BooleanField()
    subscription_id = StringField()
    stripe_id = StringField()
    created_at = DateField()
    updated_at = DateField()
