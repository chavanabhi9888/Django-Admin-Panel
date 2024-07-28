
from django.db import models

# Create your models here.
class trainer(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    gym_id=models.IntegerField()
    diet_plan=models.CharField(max_length=400)
    contact=models.IntegerField()
    