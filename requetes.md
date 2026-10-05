# 1 les offres des entreprises situées à Sokodé ;
>>> Offre.objects.filter(entreprise__ville="Sokodé")

# 2. les étudiants qui possèdent la compétence « Django » ;
>>> Etudiant.objects.filter(competences__libelle="Django").values("id", "nom", "prenom")

# 3. les candidatures d’un étudiant donné, en partant de l’objet étudiant ;
>>> etudiant=Etudiant.objects.get(nom="Kossi")
>>> etudiant.candidatures.all().values("offre","statut")

# 4. le nombre de candidatures retenues, sans charger les candidatures en mémoire ;
>>> Candidature.objects.filter(statut="Retenue").count()

# 5. les stages dont l’offre vient d’une entreprise de Sokodé ;
>>> Stage.objects.filter(candidature__offre__entreprise__ville="Sokodé").values("sujet")

# 6. les offres qui demandent au moins une compétence que possède un étudiant donné.

>>> Offre.objects.filter(competences__etudiants__nom="Assih").values("titre")