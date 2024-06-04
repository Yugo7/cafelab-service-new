from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class Product(Document):
    _id = ObjectIdField()
    name = StringField()
    description = StringField()
    origin = StringField()
    grain = StringField()
    price = FloatField()
    picture = StringField()
    section = StringField()
    created_at = DateField()
    updated_at = DateField()