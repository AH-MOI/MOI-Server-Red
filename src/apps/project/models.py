from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=24)
    content = models.CharField(max_length=400)
    closing_date = models.DateField()
    writer = models.CharField(max_length=100)
    personnel = models.CharField(max_length=100)
    hashtag = models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table = "project"

