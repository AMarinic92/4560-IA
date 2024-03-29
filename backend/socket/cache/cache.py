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

class Time(Model):
    created = CharField()
    url = CharField(primary_key=True)

    class Meta:
        primary_key = CompositeKey('id', 'url')
        database = db # This model uses the "people.db" database.



def create_cache():
    db.connect()
    db.create_tables([Response])


def cache_response(response ,url):
    success = False
    responseList = response["response"]
    Time.create(url=url,time)
    for img in responseList:
        cachedResponse = Response.create(url=url ,**img)
        cachedResponse.save()
        success = (cachedResponse == 1)
    return success


def get_cached_response(url):
    result = {}
    list = []
    query = Response.select(Response).where(Response.url == url)
    for item in query:
        obj ={"id":item.id ,"imageUrl":item.imageUrl,"type":item.type,"message":item.message,"suggestion":item.message}
        list.append(obj)
    if(len(list) == 0):
        result = None
    else:
        result["response"] = list
    print(result)
    print("done")
    return result
        


