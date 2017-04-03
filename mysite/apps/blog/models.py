from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=140)
    desc = models.TextField(default='')
    body = models.TextField()
    pub_date = models.DateTimeField()
    read_time = models.IntegerField()
    tags = TaggableManager()

    def __str__(self):
        return self.title
