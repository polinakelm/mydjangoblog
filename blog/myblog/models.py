from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    verified = models.BooleanField(default=False)