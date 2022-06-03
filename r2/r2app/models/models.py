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