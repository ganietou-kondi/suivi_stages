## Point de depart
# 1- un modele par fichier

* a- Django repond **No changes detected**.
Comment django identidie un modele :
Cela vous apprend que Django ne se base pas du tout sur le nom ou l'emplacement physique des fichiers .py pour identifier ses modèles, mais uniquement sur le chemin d'importation Python final au sein de l'application.Puisque le fichier __init__.py réexporte fidèlement la classe sous la même étiquette (stages.models.Entreprise), Django retrouve exactement la même signature en mémoire lors de son inspection. Pour l'architecture interne de Django, la structure du code n'a subi aucun changement.

Qu'est-ce que cela vous apprend sur ce qu'est une migration ?
Cela prouve qu'une migration ne suit pas l'organisation de vos fichiers de code source, mais uniquement l'état structurel et logique de la base de données.Tant que les classes de vos modèles décrivent les mêmes tables, les mêmes colonnes et les mêmes types de données, Django estime que la base de données n'a pas à évoluer. Une migration est donc une couche d'abstraction purement liée au schéma de données, totalement décorrélée des choix de découpage et de refactorisation de votre code Python.


# 2- 
# 2.2 - Ce qu'elle ne dit pas 

* Non personne ne doit pas avoire sa propre table. 
* le tuteur  appartien aussi a une entreprise pas seulement au stage qu'il encadre, car c'est l'entreprise qui designe le tuteur qui va suivre le stage
* OUI, car 2 etudiant peuvent etre accepter a un meme stage si l'entreprise veut plus d'un stgaiare
Non un stage ne peut pas etre accepter sans candidature, le champs statut au niveau de la base de donnee

* en creant une cle unique netre une offre et un etudiant au niveau de la base de donnee

* Promotion: un nombre 

* statut d'une candidature: une liste fermee 
* On ne peut pas supprimer un etudiant qui a candidater a une offre
* On ne peut pas supprimmer une offre sur laquelle un etudiant a prise
* On ne peut pas supprimer un stage qui est un candidature
* On ne peut pas supprimer une entreprise qui possede au moins un ensignant referant ou un tutuer ou qui a publier des offres
* On ne peut pas supprimer un tuteur ou un enseignat si il suit un stage 
* on ne peut pas supprimer une entreprise qui a publié des offres, pour ne pas effacer leur historique »
