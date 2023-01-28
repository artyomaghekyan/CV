from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=5000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    experience = models.TextField(max_length=5000)
    skills = models.TextField(max_length=5000)

    def __str__(self) -> str:
        return self.name
