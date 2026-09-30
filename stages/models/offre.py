from django.db import models

from .competence import Competence


class Offre(models.Model):
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    date_Debut = models.DateField()
    date_fin = models.DateField()
    nb_place = models.IntegerField()

    competence = models.ManyToManyField(
        Competence, 
        on_delete = models.SET_NULL,
        related_name= "offre"
    )


    class Meta:
        pass