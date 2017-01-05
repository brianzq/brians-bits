from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to='mysite/apps/projects/static/projects/img')

    def __str__(self):
        return self.title