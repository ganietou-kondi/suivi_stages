from django.db import models


class Personne(models.Model):

    sexe = {"F":"Femme", "H": "Homme"}  # noqa: RUF012

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    sexe = models.CharField(max_length=80, choices=sexe)
    date_naissance = models.DateField()
    email = models.EmailField()

    class Meta:
        abstract = True
        ordering = ["nom"]  # noqa: RUF012
        