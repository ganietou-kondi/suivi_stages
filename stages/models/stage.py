from django.db import models


class Stage(models.Model):
    sujet = models.CharField(max_length=150)

    tuteur_entreprise = models.ForeignKey(
        "TuteurEntreprise",
        on_delete=models.PROTECT,
        related_name="stages"
    )

    enseignant_referent = models.ForeignKey(
        "EnseignantReferent",
        on_delete=models.PROTECT,
        related_name="stages"
    )

    candidature = models.OneToOneField(
        "Candidature",
        on_delete = models.PROTECT,
        related_name="stage",
       
    )