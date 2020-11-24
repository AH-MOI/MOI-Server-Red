from django.db import models

# Create your models here.
class Participation(models.Model):

    student_id = models.ForeignKey("user.Student",on_delete=models.CASCADE)
    project_id = models.ForeignKey("project.Project",on_delete=models.CASCADE)
    student_area = models.BooleanField(default = False)
    is_passed = models.BooleanField(default = False)


    class Meta:
        db_table = "participation"

    