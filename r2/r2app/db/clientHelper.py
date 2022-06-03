from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import setup


def createClientCassandra():
    cluster = Cluster()
    setup(['127.0.0.1'], 'reddit', retry_connect=True)
    client = cluster.connect()
    setupTables(client)
    # client.execute("create keyspace reddit with replication={ 'class': 'SimpleStrategy', 'replication_factor': 2};")
    return client


def setupTables(client):
    client.execute("use reddit")
    client.execute(
        "create table if not exists thing" +
        "( id int," +
        "name text," +
        "description text," +
        "content text," +
        "create_at TIMESTAMP," +
        "updated_at TIMESTAMP," +
        "deleted_at TIMESTAMP," +
        "deleted BOOLEAN," +
        "PRIMARY KEY (id))"
    )
