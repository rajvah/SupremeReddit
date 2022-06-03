from email.policy import default
from pyexpat import model
from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField
    deleted = models.BooleanField(default=False)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
