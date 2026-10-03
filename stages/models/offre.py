from django.db import models


class Offre(models.Model):
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.IntegerField()

    competence = models.ManyToManyField(
        "Competence", 
        related_name= "offre"
    )

    entreprise = models.ForeignKey(
        "entreprise",
        on_delete=models.PROTECT,
        related_name="offres"
    )
    

    class Meta:
        pass