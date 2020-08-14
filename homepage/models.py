from django.db import models
from django.contrib.auth.models import User


# Create your models here.

"""
Author model:
Name (CharField)
Bio (TextField)
Recipe Model:
Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)
"""


class Author(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.description} - {self.author.name}'
