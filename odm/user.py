from mongoengine import Document, StringField, EmailField

class User(Document):
    name = StringField(max_lengh=250, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)