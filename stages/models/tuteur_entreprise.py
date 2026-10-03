from django.db import models

from .personne import Personne


class Tuteur_entreprise(Personne):
    entreprise = models.ForeignKey(
        "entreprise",
        on_delete=models.PROTECT,
        related_name="tuteurs_entreprise"
    )


    class Meta(Personne.Meta):
        verbose_name = "tuteur"