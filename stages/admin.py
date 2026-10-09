from django.contrib import admin

from .models.candidature import Candidature
from .models.competence import Competence
from .models.enseignant_referent import EnseignantReferent

# Register your models here.
from .models.entreprise import Entreprise
from .models.etudiant import Etudiant
from .models.offre import Offre
from .models.stage import Stage
from .models.tuteur_entreprise import TuteurEntreprise


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "ville", "secteur"]  # noqa: RUF012
    search_fields = ["nom", "ville"]  # noqa: RUF012


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "sexe", "promotion"]  # noqa: RUF012
    search_fields = ["nom", "prenom", "matricule"]  # noqa: RUF012


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ["statut", "date_depot"]  # noqa: RUF012
    search_fields = ["statut", "date_depot"]  # noqa: RUF012

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ["libelle"]  # noqa: RUF012
    search_fields = ["libelle"]  # noqa: RUF012

@admin.register(EnseignantReferent)
class Enseignant_referentAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom"]  # noqa: RUF012
    search_fields = ["nom", "prenom"]  # noqa: RUF012

@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ["titre", "date_debut", "date_fin"]  # noqa: RUF012
    search_fields = ["titre", "date_debut", "date_fin"]  # noqa: RUF012


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ["sujet", "tuteur_entreprise", "enseignant_referent"]  # noqa: RUF012
    search_fields = ["sujet"]  # noqa: RUF012

@admin.register(TuteurEntreprise)
class Tuteur_entrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "entreprise"]  # noqa: RUF012
    search_fields = ["nom", "entreprise"]  # noqa: RUF012






