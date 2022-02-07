from django.db import models


# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)


def __str__(self):
    return self.email


class Thumb(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=255)
