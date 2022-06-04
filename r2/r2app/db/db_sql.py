from r2app.models.models import Thing

def createThing(thing):
    print("db_sql:createThing method called", thing)
    assert isinstance(thing, Thing)
    thing.save()
    return thing

def getThing(id_):
    print("db_sql:getThing method called", id_)
    thing = Thing.objects.filter(id = id_)
    if(isinstance(thing, Thing)):
        return thing
    else:
        return None

def updateThing(thing):
    print("db_sql:updateThing method called", thing)
    assert isinstance(thing, Thing)
    thing.save(force_update=True)
    return thing.updated_at

def deleteThing(id_):
    print("db_sql:deleteThing method called", id_)
    thing = getThing(id_)
    if(thing is not None and isinstance(thing, Thing)):
        thing.delete()
        return True
    else:
        return False
