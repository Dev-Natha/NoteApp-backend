from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
# class Todos(models.Model):
#     details = models.TextField(max_length=250, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title