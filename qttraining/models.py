import mongoengine as mongo
from mongoengine.django.auth import User
from datetime import datetime
import binascii
import os


class Chat(mongo.Document):
    sent_on = mongo.DateTimeField()
    name = mongo.StringField()
    text = mongo.StringField()
