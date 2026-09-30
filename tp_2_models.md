## Point de depart
# 1- un modele par fichier

* a- Django repond **No changes detected**.
Comment django identidie un modele :
Cela vous apprend que Django ne se base pas du tout sur le nom ou l'emplacement physique des fichiers .py pour identifier ses modèles, mais uniquement sur le chemin d'importation Python final au sein de l'application.Puisque le fichier __init__.py réexporte fidèlement la classe sous la même étiquette (stages.models.Entreprise), Django retrouve exactement la même signature en mémoire lors de son inspection. Pour l'architecture interne de Django, la structure du code n'a subi aucun changement.

Qu'est-ce que cela vous apprend sur ce qu'est une migration ?
Cela prouve qu'une migration ne suit pas l'organisation de vos fichiers de code source, mais uniquement l'état structurel et logique de la base de données.Tant que les classes de vos modèles décrivent les mêmes tables, les mêmes colonnes et les mêmes types de données, Django estime que la base de données n'a pas à évoluer. Une migration est donc une couche d'abstraction purement liée au schéma de données, totalement décorrélée des choix de découpage et de refactorisation de votre code Python.


