from django.db import models

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# Create your models here.
class Thing(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField
    deleted = models.BooleanField(default=False)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)

class CassandraThing(Model):
   id = columns.Integer(primary_key=True)
   name = columns.Text()
   description = columns.Text()
   content = columns.Text()
   create_at = columns.DateTime()
   updated_at = columns.DateTime()
   deleted_at = columns.DateTime
   deleted = columns.Boolean(default=False)

   def __init__(self, thing, id_ = 0):
      super().__init__()
      assert isinstance(thing, Thing) and isinstance(id_, int)
      
      if(id_ == 0):
         id_ = thing.id
      self.id = id_
      self.name = thing.name
      self.description = thing.description
      self.content = thing.content
      self.create_at = thing.created_at
      self.updated_at = thing.updated_at
      self.deleted_at = thing.deleted_at
      self.deleted = thing.deleted
