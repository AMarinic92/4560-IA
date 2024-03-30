from peewee import *
import datetime


VALID_CACHE_TIME = 600  # seconds cache is valid for


db = SqliteDatabase('cache/responses.db')

class Time(Model):
    created = CharField()
    url = CharField(primary_key=True)

    class Meta:
        database = db # This model uses the "people.db" database.




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
   # Response.add_index(SQL('CREATE INDEX idx_url ON Response(url)'));
    db.create_tables([Response, Time])
    Response.add_index(SQL('CREATE INDEX idx_url ON Response(url)'));
   


def get_cache_time(url):
    try:
        query = Time.select(Time).where(Time.url == url).get()
        return query.created
    except:
        return None

def is_invalidate(cache_created):
    result = False
    if cache_created:
        time_created = float(cache_created)
        curr_time = datetime.datetime.timestamp(datetime.datetime.utcnow())
        time = curr_time - time_created
        if time > VALID_CACHE_TIME:
            result = True
  #  print(result)
    return result

def delete_response(url):
    query1 = Response.delete().where(Response.url == url).execute()
    query2 = Time.delete().where(Time.url == url).execute()


def cache_response(response ,url):
    success = False
    responseList = response["response"]
    curr_time = str(datetime.datetime.timestamp(datetime.datetime.utcnow()))
    Time.create(url=url ,created =curr_time)
    for img in responseList:
        cachedResponse = Response.create(url=url ,**img)
        cachedResponse.save()
        success = (cachedResponse == 1)
    return success


def get_cached_response(url):
    result = {}
    list = []
    cache_created = get_cache_time(url)
    invalidate = is_invalidate(cache_created)
    if invalidate:
        print("Delete cache")
        delete_response(url)
        result = None
    else:
 #   print(f"cache created {cache_created}")
        query = Response.select(Response).where(Response.url == url)
        for item in query:
            obj ={"id":item.id ,"imageUrl":item.imageUrl,"type":item.type,"message":item.message,"suggestion":item.suggestion}
            list.append(obj)
        if(len(list) == 0):
            result = None
        else:
            result["response"] = list
    print(result)
    print("done")
    return result
        


