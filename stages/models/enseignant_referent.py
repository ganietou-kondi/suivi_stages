from django.db import models

from .personne import Personne


class Enseignant_referent(Personne):
    pass


    class Meta(Personne.Meta):
        verbose_name = "tuteur"