import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import enum
from r2app.models.models import CassandraThing
import db.clientHelper as clientHelper
import db.db_cassandra as db_cassandra
import db.db_sql as db_sql

class DatabaseType(enum.Enum):
    MEDIA = enum.auto()
    ITEM = enum.auto()

    TYPE_COUNT = enum.auto()
    NONE = enum.auto()


class DatabaseEnum(enum.Enum):
    CASSANDRA = enum.auto()
    POSTGRESS = enum.auto()
    LITE = enum.auto()
    MONGO = enum.auto()
    ELASTIC = enum.auto()

    DB_COUNT = enum.auto()
    NONE = enum.auto()


class DatabaseRunner:

    def __init__(self, name):
        self.name_ = name
        self.created_ = False

        if self.name_ == "cassandra":
            # Build and Metadata
            self.db_enum_ = DatabaseEnum.CASSANDRA
            self.db_type_ = DatabaseType.MEDIA
            self.build = clientHelper.createClientCassandra

            # CRUD Function pointers
            self.create = db_cassandra.createThing
            self.read = db_cassandra.getThing
            # self.update = db_cassandra.updateThing
            self.delete = db_cassandra.deleteThing

        elif self.name_ == "lite":
            # Build and Metadata
            self.db_enum_ = DatabaseEnum.LITE
            self.db_type_ = DatabaseType.ITEM
            self.build = clientHelper.createClientSQL

            # CRUD Function pointers
            self.create = db_sql.createThing
            self.read = db_sql.getThing
            self.update = db_sql.updateThing
            self.delete = db_sql.deleteThing

        else:
            print("invalid input params")

    def createDatabase(self):
        if not self.created_:
            self.build()
            self.created_ = True
            return True
        return False


class DatabaseWrapper:
    """
   Cassandra for Query and Media (MEDIA)
   SQL for save (ITEM)
   """

    def __init__(self) -> None:
        self.db_items_ = None
        self.db_media_ = None
        self.setItemDatabase("lite")
        self.setMediaDatabase("cassandra")

    def setItemDatabase(self, db_string):
        if (self.db_items_ == None or db_string != self.db_items_.name_):
            self.db_items_ = DatabaseRunner(db_string)
            self.db_items_.build()
            return True
        else:
            return False

    def setMediaDatabase(self, db_string):
        if (self.db_media_ == None or db_string != self.db_media_.name_):
            self.db_media_ = DatabaseRunner(db_string)
            self.db_media_.build()
            return True
        else:
            return False

    def create(self, thing):
        id = self.db_items_.create(thing)
        ct = CassandraThing(thing, id)
        self.db_media_.create(ct)
        return id

    def read(self, id):
        return self.db_media_.read(id)

    def update(self, thing):
        updated_at = self.db_items_.update(thing)
        ct = CassandraThing(thing, thing.id)
        self.db_media_.update(ct)
        return updated_at

    def delete(self, id):
        retval1 = self.db_media_.delete(id)
        retval2 = self.db_items_.delete(id)
        return retval1 and retval2
