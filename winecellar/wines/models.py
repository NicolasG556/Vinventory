from django.db import models
from django.conf import settings
from PIL import Image


class CaveVirtuelle(models.Model):
    nom = models.CharField(max_length=50)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class RegionViticole(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=500)
    longitude = models.FloatField(default=1.0)
    latitude = models.FloatField(default=1.0)

    def __str__(self):
        return self.nom


class Vin(models.Model):
    class Couleur(models.TextChoices):
        ROUGE = 'ROUGE'
        BLANC = 'BLANC'
        ROSE = 'ROSÉ'

    nom = models.CharField(max_length=50)
    millesime = models.IntegerField()
    couleur = models.fields.CharField(choices=Couleur.choices, max_length=6)
    domaine = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    id_region = models.ForeignKey(RegionViticole, on_delete=models.CASCADE)
    id_cave = models.ForeignKey(CaveVirtuelle, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Cepage(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.nom


class Met(models.Model):
    nom = models.CharField(max_length=50)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.nom


class Photo(models.Model):
    image = models.ImageField(verbose_name='image')
    caption = models.CharField(max_length=200, blank=True)

    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    dateHeure = models.DateTimeField()
    description = models.TextField(max_length=1000)
    image = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    nbPlaces = models.IntegerField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)

    def __str__(self):
        return self.nom
