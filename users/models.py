from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, verbose_name='имя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []