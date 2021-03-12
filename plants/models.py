from django.db import models


# Create your models here.
class Plant(models.Model):
    title = models.CharField(max_length=100, null=True)
    botanical_name = models.CharField(max_length=100, null=True)
    plant_type = models.CharField(max_length=100, null=True)
    mature_size = models.CharField(max_length=100, null=True)
    sun_exposure = models.CharField(max_length=100, null=True)
    soil_type = models.CharField(max_length=100, null=True)
    hardiness_zones = models.CharField(max_length=100, null=True)
    native_area = models.CharField(max_length=100, null=True)
    toxicity = models.CharField(max_length=100, null=True)
    notes = models.TextField(null=True)
    image = models.CharField(max_length=100, null=True)
