from peewee import *

db = SqliteDatabase('cache/responses.db')

class Response(Model):
    id = CharField()
    imageUrl = CharField()
    type = CharField()
    message = CharField()
    suggestion  = CharField()
    

    class Meta:
        database = db # This model uses the "people.db" database.



def create_cache():
    db.connect()
    db.create_tables([Response])


def cache_response(response):
    success = False
    responseList = response["response"]
    for img in responseList:
        cachedResponse = Response.create(**img)
        cachedResponse.save()
        success = (cachedResponse == 1)
    return success


