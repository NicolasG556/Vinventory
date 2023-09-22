from django.db import models


class CaveVirtuelle(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class RegionViticole(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.nom


class Vin(models.Model):
    nom = models.CharField(max_length=50)
    millesime = models.IntegerField()
    couleur = models.CharField(max_length=20)
    domaine = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    id_region = models.ForeignKey(RegionViticole, on_delete=models.CASCADE)

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
