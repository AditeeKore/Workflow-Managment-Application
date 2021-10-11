from django.db import models
from django.contrib.auth.models import User

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
    
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
	    return self.text


