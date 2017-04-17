from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=100)
    desc = models.TextField(default='')
    body = models.TextField()
    pub_date = models.DateTimeField()
    read_time = models.IntegerField()
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
