from django.db import models

from .personne import Personne


class Enseignant_referent(Personne):


    class Meta(Personne.Meta):
        pass