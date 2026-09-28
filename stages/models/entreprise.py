from django.db import models

# Create your models here.

class Entreprise(models.Model):
    """Une entreprise succeptible d'acceullire un stagiaire"""

    secteurs = {"I": "informatique", "G": "gestion",}  # noqa: RUF012

    nom = models.CharField(max_length=120)
    ville = models.CharField(max_length=80)
    secteur = models.CharField(max_length=80, choices=secteurs)
    contact = models.EmailField()
    email = models.EmailField()


    class Meta:
        ordering = ["nom"]  # noqa: RUF012
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"
        constraints = [models.UniqueConstraint(fields=["nom", "ville"], name="nom_ville")]  # noqa: RUF012




    def __str__(self):
        return f"{self.nom} ({self.ville})"





        