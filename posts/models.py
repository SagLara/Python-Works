"""Posts models."""
#Django
from django.db import models

# Create your models here.
class User(models.Model):
    """User model"""

    email= models.EmailField(unique=True)
    password= models.CharField(max_length=50)

    first_name=models.CharField(max_length=50)
    second_name=models.CharField(max_length=50)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.TextField(blank=True, null=True)

    city=models.CharField(max_length=50, null=True)
    country=models.CharField(max_length=50, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
