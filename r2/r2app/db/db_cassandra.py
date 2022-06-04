import db.clientHelper as clientHelper

CASS_CLIENT = clientHelper.createClientCassandra()

def createThing(thing):
    return CASS_CLIENT.execute(
        "INSERT INTO thing (id, name, description, content, create_at, updated_at)"
        + "VALUES (%s,%s,%s,%s,%s,%s)", [
            thing.id, thing.name, thing.description, thing.content,
            thing.create_at, thing.updated_at
        ])

def getThing(id):
    return CASS_CLIENT.execute("SELECT * FROM thing WHERE id=?", [id]).one()

def deleteThing(id):
    return CASS_CLIENT.execute("DELETE from thing where id=?", [id])
