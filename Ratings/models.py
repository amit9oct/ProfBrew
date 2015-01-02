from django.db import models

# Create your models here.
class Ratings(models.Model):
    _no_of_likes=models.BigIntegerField(null=False)
    
    