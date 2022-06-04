import db.clientHelper as clientHelper

CASS_CLIENT = clientHelper.createClientCassandra()


def createThing(thing):
    print("db_cassandra:createThing method called", thing)
    return CASS_CLIENT.execute(f'INSERT INTO thing (id) VALUES ({thing.id})')

def getThing(id):
    print("db_cassandra:getThing method called", id)
    return CASS_CLIENT.execute(f'SELECT * FROM thing WHERE id={id}').one()

def updateThing(thing):
    print("db_cassandra:getThing method called", thing)
    return thing.updated_at

def deleteThing(id):
    print("db_cassandra:deleteThing method called", id)
    return CASS_CLIENT.execute(f'DELETE from thing where id={id}')
