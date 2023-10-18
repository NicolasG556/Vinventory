from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonnné'),
        (ADMIN, 'Administrateur'),
    )

    profile_photo = models.ImageField(null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
