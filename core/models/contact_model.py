from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class Contact(Document):
    _id = ObjectIdField()
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    phone = StringField()
    description = StringField()
    created_at = DateField()