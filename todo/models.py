from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name="tasks")
    task = models.CharField(max_length=500)
    task_description = models.TextField()
    is_done = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    done_date = models.DateTimeField(auto_now=True)

