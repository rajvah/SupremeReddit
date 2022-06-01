from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Thing(models.Model):
    name: models.CharField(max_length=255)
    description: models.CharField
    content: models.CharField
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)
    deleted_at: models.DateTimeField
    deleted: models.BooleanField(default=False)

class Subreddit(Thing):
    subscriber_count: models.IntegerField(default=0)

class Post(Thing):
    subreddit: models.ForeignKey(Subreddit)
    upvote_count: models.IntegerField(default=0)
    downvote_count: models.IntegerField(default=0)

class Comment(Thing):
    post: models.ForeignKey(Post)
    upvote_count: models.IntegerField(default=0)
    downvote_count: models.IntegerField(default=0)
    comment_tree: models.ManyToManyField('self', blank=True, symmetrical=False)