from django.db import models

# Create your models here.

class Country(models.Model):
    country_name=models.CharField(max_length=30,primary_key=True)
    country_code=models.IntegerField(unique=True, null=True)
    region=models.CharField(max_length=30)

class Capital(models.Model):
    capital_name=models.CharField(max_length=30,primary_key=True)
    country_name=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_code=models.IntegerField(unique=True,null=True)
    