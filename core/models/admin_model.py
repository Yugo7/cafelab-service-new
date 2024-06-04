from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class Admin(Document):
    _id = ObjectIdField()
    name = StringField()
    email = StringField()
    password = StringField()
    created_at = DateField()
    updated_at = DateField()
