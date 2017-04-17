from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=100)
    desc = models.TextField(default='')
    body = models.TextField()
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to='projects/img')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title