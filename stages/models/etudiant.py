from django.db import models

from .personne import Personne


class Etudiant(Personne):
    matricule = models.CharField(max_length = 150)
    promotion = models.IntegerField()

    competences = models.ManyToManyField(
        "Competence",
        related_name="etudiants"
    )

    class Meta(Personne.Meta):
        verbose_name = "etudiant"


        

    
