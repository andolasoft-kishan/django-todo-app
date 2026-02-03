from django.db import models
from django.contrib.auth.models import User # Import the User model

class Todo(models.Model):
    # Link each task to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.title