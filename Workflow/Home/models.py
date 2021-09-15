from django.db import models

# Create your models here.
class Assigned_tasks(models.Model):
    task_no = models.CharField(max_length=10)
    task_name = models.CharField(max_length=50)
    task_desc = models.CharField(max_length=700, null=True)
    assigned_to = models.CharField(max_length=50)
    submit_time = models.TimeField()
    submit_date = models.DateField(null=True)
    def __str__(self):
        return self.task_name
    
class Registration(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    def __str__(self):
        return self.username