import clientHelper
import datetime
from r2app.models.models import CassandraThing

def createThing(thing):
    res = client.execute(
        "INSERT INTO thing (id,name, description, content, create_at, updated_at)" +
        "VALUES (%s,%s,%s,%s,%s,%s)",
        [thing.id, thing.name, thing.description, thing.content, thing.create_at, thing.updated_at])
    print(res)
    
def getThing(id):
    res = client.execute("SELECT * FROM thing WHERE id=?", [id]).one()
    return res

# def updateThing(thing):
#     res = client.execute(
#         "update thing "
#     )

def deleteThing(id):
    res = client.execute("DELETE from thing where id=?", [id])


#Test
def main():
    thing = CassandraThing.Thing.create(
        id=1,
        name="Harshit",
        description="sample",
        content="test",
        create_at=datetime.date.today(),
        updated_at=datetime.date.today(),
    )
    createThing(thing)

if __name__ == "__main__":
    client = clientHelper.createClientCassandra()
    main()