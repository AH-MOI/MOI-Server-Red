from django.db import models

# Create your models here.
class User(models.Model):

    id = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=12)
    birthday = models.DateField()
    school = models.CharField(max_length=4)
    profile = models.CharField(max_length=128)
    github = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    area=models.CharField(max_length=24)
    hashtag=models.CharField(max_length=40)


    

