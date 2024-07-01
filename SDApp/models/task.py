from django.db import models
from .user import CustomUser


class Task(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    due_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
