from django.db import models

from .offre import Offre


class Competence(models.Model):
    libelle = models.CharField(max_length=150)
    offre = models.ManyToManyField(
        Offre,
        on_delete = models.SET_NULL,
        related_name="competences"
    )

    class Meta:
        pass