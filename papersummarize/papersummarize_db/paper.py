from mongoengine import *


class Paper(Document):
    sid = StringField()
    source = StringField()
    authors = ListField(StringField())
    title = StringField()
    link = StringField()

    data = DictField()
