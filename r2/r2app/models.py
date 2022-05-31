from pyexpat import model
from django.db import models

# Create your models here.
class Thing(models.Model):
    title: models.CharField(max_length=255)
    description: models.CharField
    content: models.CharField
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)
    deleted_at: models.DateTimeField
    deleted: models.BooleanField(default=False)
