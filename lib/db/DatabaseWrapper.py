from thing import Thing
import tdb_sql as post
from tdb_cassandra import Thing as MediaThing

import enum

class DatabaseEnum(enum.Enum):
      NONE = enum.auto()
      CASSANDRA = enum.auto()
      POSTGRESS = enum.auto()
      LITE = enum.auto()
      # MONGO = enum.auto()
      # ELASTIC = enum.auto()

class DatabaseWrapper:
   """
   Cassandra for Query and Media (MEDIA)
   Posgress for save (ITEM)
   """

   """
   Map each of the _cache_prefix to an enumerated value
   """
   database_list_ = {
      "tdbcassandra_" : DatabaseEnum.CASSANDRA,
      "thing_" : DatabaseEnum.POSTGRESS,
      "tdb_lite" : DatabaseEnum.LITE,
   }
   def __init__(self) -> None:
      self.query_db = DatabaseEnum.NONE
      self.media_db = DatabaseEnum.NONE

      self.setQueryDatabase("postgress")
      self.setMediaDatabase("cassandra")

   def setQueryDatabase(self, db_string):
      if(self.database_list_.__contains__(db_string)):
         self.query_db = self.database_list_[db_string]
         return True
      else:
         return False

   def setMediaDatabase(self, db_string):     
      if(self.database_list_.__contains__(db_string)):
         self.media_db = self.database_list_[db_string]
         return True
      else:
         return False

   def getDatabaseType(self, thing):
      assert(isinstance(thing, Thing))
      return self.database_list_[thing._cache_prefix]

   def create(self, thing, db_selection = None):
      assert isinstance(thing, Thing) or isinstance(thing, MediaThing)
      if(db_selection == None):
         db_selection = self.getDatabaseType(thing)
      
      if (db_selection != DatabaseEnum.NONE):
         return False

      # this will write the thing to the database
      # Stack:
      #     tdb.make_thing() - only for tdb_SQL
      #     tdb.get_thing_table
      if (isinstance(thing, Thing)):
         new_id = thing.write_new_thing_to_db()
      elif (isinstance(thing, MediaThing)):
         # TODO: (Howard, Chase) how to add MediaThing to Cassandra
         new_id = 0
      return new_id

   # this is at the level of the tdb_sql
   def _db_insert(thing):
      assert isinstance(thing, Thing)
      table = post.get_thing_table(thing.__class__._type_id,
                           ups=thing._ups,
                           downs=thing._downs,
                           date=thing._date,
                           deleted=thing._deleted,
                           spam=thing._spam,
                           )

      params = dict(ups = thing._ups, downs = thing._downs,
                  date = thing._date, deleted = thing._deleted, spam = thing._spam)

      if id:
        params['thing_id'] = id

      # TODO: this is where the database is bound and added
      # transactions.add_engine(table.bind)
      r = table.insert().execute(**params)
      new_id = r.inserted_primary_key[0]
      new_r = r.last_inserted_params()
      for k, v in params.iteritems():
         if new_r[k] != v:
            raise Exception("There's shit in the plumbing. " +
                                 "expected %s, got %s" % (params,  new_r))
      return new_id

   """
   Description: gets the item from the specified save_db by the _id, with the
   specified table of the item from the arguments passed

   Parameters: _id is the unique identifier of the item, args should contain
   the table the save_db should retrieve the item from
   
   Returns: the specified item by the unique _id

   Exceptions: large media files (which will be stored in their own tables)
   will be handled separately by the media_db and cannot be specified as the
   table type in the args, the other table types and id must exist in the
   table, otherwise will throw an exception
   """
   def get_item(self, _id = None, **args):
      pass

   """
   Description: creates the item with the specified args parameters and fields
    specified for the table specified in the args
   Parameters: args should have valid data values for the specified key-value 
   pairs for the specified table for the item 
   Returns: True if the item saved successfully in the save_db, False otherwise
   Exceptions: must have valid parameters specified in key-value pairs for the 
   specified table for the item
   """
   def create_item(self, **args):
      pass

   """
   Description: updates the item with the unique _id, with values passed 
   through in the args for the specified item table
   Parameters: _id as the unique identifier of the item, with args containing 
   the updated values for the specified item table
   Returns: True if the item updated successfully in the save_db, False 
   otherwise
   Exceptions: must have valid parameters specified in key-value pairs for the 
   specified table for the item and an _id that exists in the table for that 
   item table 
   """
   def update_item(self, _id = None, **args):
      pass

   """
   Description: deletes the item with the unique _id of the item table 
   specified in args. Any related associations to the deleted item should be 
   removed and reference ids set to None

   Parameters: _id as the unique identifier of the item, with args containing 
   the specified item table
   Returns: True if the item deleted successfully in the save_db, False 
   otherwise
   Exceptions: must have valid item table and an _id that exists in the table 
   for that item table 
   """
   def delete_item(self, _id = None, **args):
      pass

   """
   Description: searches the specified query_db for the specific item table or 
   any related item tables passed through in args. The arguments can also pass 
   in query-specific fields and their values in the tables as well
   Parameters: args determines the table(s) searched in the query_db and any 
   potential key-value pairs specified in the tables. The args can also dictate
   any pagination, sort-order, sort-by (specific field), and other 
   search-function parameters as well. The exact_match determines whether or 
   not the specified query should be exactly matched or similarly matched 
   (which could take a longer time from the data level)
   Returns: a list of items as the search results of the request (default or 
   error will return an empty list)
   Exceptions: must have valid item table available for search and the 
   specified key-value pairs to match the search
   """
   def search_items(self, exact_match = True, **args):
      pass
   
   """
   Description: gets the related media content (stored in the media_db 
   specified for faster processing of media data) but specified unique id or 
   any related table ids
   Parameters: _id is the unique identifier of the media table, _rel_id 
   specifies any related items the media may be associated with (i.e. Reddit 
   posts may have images and videos as parts of their thread), args
   Returns: the specified media file by the unique _id or _rel_id 
   Exceptions: the media table types and id or related id must exist in the 
   table, otherwise will throw an exception
   """
   def get_media(self, _id = None, _rel_id = None, **args):
      pass

   """
   Description: creates the media with the specified args parameters and fields
   specified for the table specified in the args. Creates the related item id 
   as an association if specified.
   Parameters: args should have valid data values for the specified key-value 
   pairs for the specified table for the item, if _rel_id is passed, will 
   associate the media to the related item id 
   Returns: True if the media saved successfully in the media_db, False 
   otherwise
   Exceptions: must have valid parameters specified in key-value pairs for the 
   specified table for the media and valid _rel_id for the item association
   """
   def create_media(self, _rel_id = None, **args):
      pass

   """
   Description: updates the media with the unique _id, with values passed 
   through in the args for the specified media table or association with 
   _rel_id
   Parameters: _id as the unique identifier of the media with args containing 
   the updated values for the specified media table and can associate with a 
   _rel_id item
   Returns: True if the media updated successfully in the media_db, False 
   otherwise
   Exceptions: must have valid parameters specified in key-value pairs for the 
   specified table for the media and an _id that exists and valid _rel_id for 
   the item association
   """
   def update_media(self, _id = None, _rel_id = None, **args):
      pass

   """
   Description: deletes the media with the unique _id of the media table 
   specified in args. Any related associations to the deleted item should be 
   removed and reference ids set to None
   Parameters: _id as the unique identifier of the media, with args containing 
   the specified media table
   Returns: True if the media deleted successfully in the media_db, False 
   otherwise
   Exceptions: must have valid media _id that exists and valid _rel_id for the 
   item association 
   """
   def delete_media(self, _id = None, _rel_id = None, **args):
      pass

   """
   Description: searches the specified query_db for the specific media table or
   any related media tables passed through in args. The arguments can also pass
   in query-specific fields and their values in the tables as well
   Parameters: args determines the table(s) searched in the query_db and any 
   potential key-value pairs specified in the tables. The args can also dictate
   any pagination, sort-order, sort-by (specific field), and other 
   search-function parameters as well. The exact_match determines whether or 
   not the specified query should be exactly matched or similarly matched 
   (which could take a longer time from the data level)
   Returns: a list of medias as the search results of the request (default or 
   error will return an empty list)
   Exceptions: must have valid media table available for search and the 
   specified key-value pairs to match the search
   """
   def search_media(self, _rel_id = None, **args):
      pass

   @classmethod
   def get_things_from_cache(cls, ids, stale=False, allow_local=True):
      """Read things from cache and return id->thing dict."""
      cache = cls._cache
      prefix = cls._cache_prefix()
      things_by_id = cache.get_multi(
         ids, prefix=prefix, stale=stale, allow_local=allow_local,
         stat_subname=cls.__name__)
      return things_by_id

   @classmethod
   def write_things_to_cache(cls, things_by_id):
      """Write id->thing dict to cache.

      Used to populate the cache after a cache miss/db read. To ensure we
      don't clobber a write by another process (we don't have a lock) we use
      add_multi to only set the values that don't exist.

      """

      cache = cls._cache
      prefix = cls._cache_prefix()
      try:
         cache.add_multi(things_by_id, prefix=prefix, time=cls._cache_ttl)
      except:
         raise ("write_things_to_cache error")

   def write_changes_to_db(self, changes, brand_new_thing=False):
      """Write changes to db."""
      if not changes:
         return

      data_props = {}
      props = {}
      for prop, (old_value, new_value) in changes.iteritems():
         if prop.startswith('_'):
               props[prop[1:]] = new_value
         else:
               data_props[prop] = new_value

      self.write_props_to_db(props, data_props, brand_new_thing)

   def write_thing_to_cache(self, lock, brand_new_thing=False):
      """After modifying a thing write the entire object to cache.

      The caller must either pass in the read_modify_write lock or be acting
      for a newly created thing (that has therefore never been cached before).

      """

      assert brand_new_thing or lock.have_lock

      cache = self.__class__._cache
      key = self._cache_key()
      cache.set(key, self, time=self.__class__._cache_ttl)

   def update_from_cache(self, lock):
      """Read the current value of thing from cache and update self.

      To be used before writing cache to avoid clobbering changes made by a
      different process. Must be called under write lock.

      """

      assert lock.have_lock

      # disallow reading from local cache because we want to pull in changes
      # made by other processes since we first read this thing.
      other_selfs = self.__class__.get_things_from_cache(
         [self._id], allow_local=False)
      if not other_selfs:
         return
      other_self = other_selfs[self._id]

      # update base_props
      for base_prop in self._base_props:
         other_self_val = getattr(other_self, base_prop)
         self.__setattr__(base_prop, other_self_val, make_dirty=False)

      # update data_props
      self._t = other_self._t

      # reapply changes made to self
      self_changes = self._dirties
      self._dirties = {}
      for data_prop, (old_val, new_val) in self_changes.iteritems():
         setattr(self, data_prop, new_val)  

   def _commit(self):
        """Write changes to db and write the full object to cache.

        When writing to postgres we write only the changes. The data in 
        postgres is the canonical version.

        For a few reasons (speed, decreased load on postgres, postgres
        replication lag) we want to keep a perfectly consistent copy of the
        thing in cache.

        To achieve this we read the current value of the thing from cache to
        pull in any changes made by other processes, apply our changes to the
        thing, and finally set it in cache. This is done under lock to ensure
        read/write safety.

        If the cached thing is evicted or expires we must read from postgres.

        Failure cases:
        * Write to cache fails. The cache now contains stale/incorrect data. To
          ensure we recover quickly TTLs should be set as low as possible
          without overloading postgres.
        * There is long replication lag and high cache pressure. When an object
          is modified it is written to cache, but quickly evicted, The next
          lookup might read from a postgres secondary before the changes have
          been replicated there. To protect against this replication lag and
          cache pressure should be monitored and kept at acceptable levels.
        * Near simultaneous writes that create a logical inconsistency. Say
          request 1 and request 2 both read state 0 of a Thing. Request 1
          changes Thing.prop from True to False and writes to cache and
          postgres. Request 2 examines the value of Thing.prop, sees that it is
          True, and due to logic in the app sets Thing.prop_is_true to True and
          writes to cache and postgres. Request 2 didn't clobber the change
          made by request 1, but it made a logically incorrect change--the
          resulting state is Thing.prop = False and Thing.prop_is_true = True.
          Logic like this should be identified and avoided wherever possible, 
          or protected against using locks.

        """
      #   if not self._created:
      #       with TdbTransactionContext():
      #           _id = self.write_new_thing_to_db()
      #           self._id = _id
      #           self._created = True

      #           changes = self._dirties.copy()
      #           self.write_changes_to_db(changes, brand_new_thing=True)
      #           self._dirties.clear()

      #       self.write_thing_to_cache(lock=None, brand_new_thing=True)
      #       self.record_cache_write(event="create")
      #   else:
      #       with self.get_read_modify_write_lock() as lock:
      #           self.update_from_cache(lock)
      #           if not self._dirty:
      #               return

      #           with TdbTransactionContext():
      #               changes = self._dirties.copy()
      #               self.write_changes_to_db(changes, brand_new_thing=False)
      #               self._dirties.clear()

      #           self.write_thing_to_cache(lock)
      #           self.record_cache_write(event="modify")

      #   hooks.get_hook("thing.commit").call(thing=self, changes=changes)
      

   """
   Below is what was written for the thing class, above is what was written
   for the DataThing class, which is the _super_ for Thing
   """
   @classmethod
   def get_things_from_db(cls, ids):
      """Read props from db and return id->thing dict."""
      props_by_id = post.get_thing(cls._type_id, ids)
      data_props_by_id = post.get_thing_data(cls._type_id, ids)

      things_by_id = {}
      for _id, props in props_by_id.iteritems():
         data_props = data_props_by_id.get(_id, {})
         thing = cls(
               ups=props.ups,
               downs=props.downs,
               date=props.date,
               deleted=props.deleted,
               spam=props.spam,
               id=_id,
         )
         thing._t.update(data_props)

         if not all(data_prop in thing._t for data_prop in cls._essentials):
                # a Thing missing an essential prop is invalid
                # this can happen if a process looks up the Thing as it's
                # created but between when the props and the data props are
                # written
               continue

         things_by_id[_id] = thing

      return things_by_id

   def write_new_thing_to_db(thing):
      """Write the new thing to db and return its id."""
      assert isinstance(thing, Thing)
      assert not thing._created

      return post.make_thing(
         type_id=thing.__class__._type_id,
         ups=thing._ups,
         downs=thing._downs,
         date=thing._date,
         deleted=thing._deleted,
         spam=thing._spam,
      )
