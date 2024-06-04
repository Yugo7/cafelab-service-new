from mongoengine import (Document, StringField, EmbeddedDocument, EmbeddedDocumentField, ObjectIdField, ListField,
                         BooleanField, FloatField, IntField, DateField)


class Orders(Document):
    _id = ObjectIdField()
    user_id = StringField()
    address = StringField()
    product_id = ListField()
    status = StringField()
    amount = FloatField()
    zip_code = StringField()
    created_at = DateField()
    updated_at = DateField()
