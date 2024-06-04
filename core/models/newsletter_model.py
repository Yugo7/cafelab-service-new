from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class Newsletter(Document):
    _id = ObjectIdField()
    email = StringField()