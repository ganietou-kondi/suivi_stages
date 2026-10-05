from django.db import models


class Offre(models.Model):
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nb_places = models.IntegerField()

    competences = models.ManyToManyField(
        "Competence", 
        related_name= "offre"
    )

    entreprise = models.ForeignKey(
        "Entreprise",
        on_delete=models.PROTECT,
        related_name="offres"
    )
    

    class Meta:
        pass