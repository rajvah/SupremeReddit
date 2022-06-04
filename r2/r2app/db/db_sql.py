import clientHelper
from ..models.models import Thing

def createThing(thing):
    assert isinstance(thing, Thing)
    thing.save(force_insert=True)
    return thing.id

def getThing(id_):
    thing = Thing.objects.filter(id = id_)
    if(isinstance(thing, Thing)):
        return thing
    else:
        return None

def updateThing(thing):
    assert isinstance(thing, Thing)
    thing.save(force_update=True)
    return thing.updated_at

def deleteThing(id):
    thing = getThing(id)
    if(thing is not None and isinstance(thing, Thing)):
        thing.delete()
        return True
    else:
        return False
