from django.db import models

from .personne import Personne


class Tuteur_entreprise(Personne):
    pass


    class Meta(Personne.Meta):
        verbose_name = "tuteur"