from django.db import models

from .personne import Personne


class Etudiant(Personne):
    matricule = models.CharField(max_length = 150)
    promotion = models.CharField(max_length=150)

    candidature = models.ForeignKey(
        'Candidature', on_delete=models.SET_NULL,  
        related_name="etudiant"
    )




    class Meta(Personne.Meta):
        verbose_name = "etudiant"


        

    
