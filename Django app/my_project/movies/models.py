from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
#MOvie checklist
#cast List

class Cast_List(models.Model):
    cast_name = models.CharField(max_length=200)
    def __str__(self):
        return self.cast_name

class Movies_list(models.Model):
    movie_name =  models.CharField(max_length=200)
    rating = models.FloatField(null=True, blank=True, default=None)
    year = models.IntegerField(default= None ,null=True,blank=True)
    cast = models.ManyToManyField(Cast_List, null=True, blank=True)
    def __str__(self):
        return self.movie_name
