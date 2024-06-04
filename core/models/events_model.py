from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class Events(Document):
    _id = ObjectIdField()
    title = StringField()
    date = StringField()
    description = StringField()
    picture = StringField()