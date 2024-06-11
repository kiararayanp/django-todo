from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    # string representation
    def __str__(self):
        return self.task
