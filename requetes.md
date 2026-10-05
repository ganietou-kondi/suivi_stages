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



1- offre1 = Offre.objects.create(titre="Developpeur web flutter", description="Developpement d'une application web avec flutter.", date_debut="2026-06-01", date_fin="2026-05-31", nb_places=2, entreprise=entreprise1)
2- offre1 = Offre.objects.create(titre="", description="Developpement d'une application web avec flutter.", date_debut="2026-06-01", date_fin="2026-05-31", nb_places=2, entreprise=entreprise1)


# 
a- Offre avec dates incohérentes : la base accepte la donnée.
Offre avec titre vide : la base accepte la donnée.
Deux candidatures pour le même étudiant et la même offre : la base refuse la deuxième candidature à cause de la contrainte UNIQUE.

b- Les deux premières situations concernent des règles de cohérence des données que la base n'empêche pas actuellement.

La date de fin devrait être postérieure à la date de début et le titre devrait être obligatoire. 
Selon moi, ces données auraient dû être refusées par le modèle Django ou par la validation de l’application, car il s’agit de règles métier.


# Restitution 

1. Suppression d’un stage et de sa candidature
J’ai choisi PROTECT entre le stage et la candidature, car on ne doit pas pouvoir supprimer une candidature qui est associée à un stage, afin de conserver l’historique du stage.

2. PROTECT est appliqué par Django, et non directement par la base de données.

Si on supprime directement une entreprise en SQL, **Django n’applique pas `PROTECT`**. L’entreprise peut donc être supprimée alors que ses offres existent encore, ce qui peut créer une incohérence.

3. La différence est que la règle d’unicité est imposée par la base de données, tandis que les règles concernant les dates et le titre sont metiers