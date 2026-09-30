from django.db import models

from .etudiant import Etudiant
from .offre import Offre
from .stage import Stage


class Candidature(models.Model):
    statut = models.CharField(max_length=150)
    date_depot = models.DateField()

    etudiant = models.ForeignKey(
        Etudiant,
        on_delete = models.SET_NULL,
        related_name="candidatures"
    )

    offre = models.ForeignKey(
        Offre,
        on_delete = models.SET_NULL,
        related_name="offres"
    )

    stage = models.OneToOneField(
        Stage,
        on_delete = models.SET_NULL,
        related_name="stage"
    )


    class Meta:
        pass