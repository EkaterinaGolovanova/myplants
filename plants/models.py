from django.db import models


# Create your models here.
class Plant(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path='/plants/img')
