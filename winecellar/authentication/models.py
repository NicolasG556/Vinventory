from django.db import models
from django.contrib.auth.models import AbstractUser
from wines.models import Photo


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonnné'),
        (ADMIN, 'Administrateur'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    profile_pic = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
