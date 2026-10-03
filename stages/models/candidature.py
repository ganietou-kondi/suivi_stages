from django.db import models


class Candidature(models.Model):

    statuts = {"Depose": "Depose", "Retenue": "Retenue", "Refuse": "Refuse",}  # noqa: RUF012

    statut = models.CharField(max_length=150, choices=statuts)
    date_depot = models.DateField(auto_now=True)


    etudiant = models.ForeignKey(
        "Etudiant", 
        on_delete=models.PROTECT,
        related_name="candidatures"
    )


    offre = models.ForeignKey(
        "Offre",
        on_delete = models.PROTECT,
        related_name="candidatures"
    )

  


    class Meta:
        constraints = [models.UniqueConstraint(fields=["etudiant", "offre"], name="offre_etudiant")]  # noqa: RUF012

       