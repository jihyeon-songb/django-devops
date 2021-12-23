from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50)
    line = models.BooleanField(default=False)