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
    is_profilepic = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (200, 200)
    PROFILE_PIC_MAX_SIZE = (100, 100)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def resize_image_profilepic(self):
        image = Image.open(self.image)
        image.thumbnail(self.PROFILE_PIC_MAX_SIZE)
        image.save(self.image.path)

    # Add a method to set this photo as a profile picture
    def set_as_profile_pic(self):
        self.is_profile_pic = True
        self.save()

    # Add a method to unset this photo as a profile picture
    def unset_as_profile_pic(self):
        self.is_profile_pic = False
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_profile_pic:  # Check if it's a profile picture
            self.resize_image_profilepic()
        else:
            self.resize_image()


class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    dateHeure = models.DateTimeField()
    description = models.TextField(max_length=1000)
    image = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    nbPlaces = models.IntegerField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.nom
