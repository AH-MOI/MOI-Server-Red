from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=24),
    content = models.CharField(max_length=400),
    closing_data = models.DateField(),
    writer = models.CharField(),
    personnel = models.CharField(),
    hashtag = models.CharField(null=True),
    profile = models.ImageField(null=True),
    

