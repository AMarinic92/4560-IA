from peewee import *

db = SqliteDatabase('cache/responses.db')

class Response(Model):
    id = CharField()
    imageUrl = CharField()
    type = CharField()
    message = CharField()
    suggestion  = CharField()
    url = CharField()
    

    class Meta:
        primary_key = CompositeKey('id', 'url')
        database = db # This model uses the "people.db" database.



def create_cache():
    db.connect()
    db.create_tables([Response])


def cache_response(response ,url):
    success = False
    responseList = response["response"]
    for img in responseList:
        cachedResponse = Response.create(url=url ,**img)
        cachedResponse.save()
        success = (cachedResponse == 1)
    return success


