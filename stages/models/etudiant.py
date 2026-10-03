from django.db import models

from .personne import Personne


class Etudiant(Personne):
    matricule = models.CharField(max_length = 150)
    promotion = models.CharField(max_length=150)

    competence = models.ManyToManyField(
        "Competence",
        related_name="etudiants"
    )

    class Meta(Personne.Meta):
        verbose_name = "etudiant"


        

    
