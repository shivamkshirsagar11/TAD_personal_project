import datetime
from django.db import models

class Task(models.Model):
    google_id = models.IntegerField(default=-1)
    task_name = models.TextField(max_length=255)
    is_completed = models.BooleanField(default=False)
    task_start_date = models.DateTimeField(datetime.datetime.now())
    task_end_date = models.DateTimeField()
    task_importance = models.IntegerField(default=0)

