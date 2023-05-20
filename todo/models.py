from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    
    
    def __str__(self):
        return self.task