from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=160)
    date = models.CharField(max_length=30)
    percent = models.IntegerField()

    def __str__(self):
        return self.text
