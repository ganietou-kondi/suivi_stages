## Point de depart
# 1- un modele par fichier

* a- Django repond **No changes detected**.
Comment django identidie un modele :
Cela vous apprend que Django ne se base pas du tout sur le nom ou l'emplacement physique des fichiers .py pour identifier ses modèles, mais uniquement sur le chemin d'importation Python final au sein de l'application.Puisque le fichier __init__.py réexporte fidèlement la classe sous la même étiquette (stages.models.Entreprise), Django retrouve exactement la même signature en mémoire lors de son inspection. Pour l'architecture interne de Django, la structure du code n'a subi aucun changement.

Qu'est-ce que cela vous apprend sur ce qu'est une migration ?
Cela prouve qu'une migration ne suit pas l'organisation de vos fichiers de code source, mais uniquement l'état structurel et logique de la base de données.Tant que les classes de vos modèles décrivent les mêmes tables, les mêmes colonnes et les mêmes types de données, Django estime que la base de données n'a pas à évoluer. Une migration est donc une couche d'abstraction purement liée au schéma de données, totalement décorrélée des choix de découpage et de refactorisation de votre code Python.


# 2- 
# 2.2 - Ce qu'elle ne dit pas 

* Non personne ne doit pas avoire sa propre table. Car la responssable ne demande jamais toutes les personne

* le tuteur  appartien aussi a une entreprise pas seulement au stage qu'il encadre, car c'est l'entreprise qui designe le tuteur qui va suivre le stage

* Non, Car une candidature si elle est accepte donne naissance a  un seul stage 
Non un stage ne peut pas etre accepter sans candidature, car le champ candidature est obligatoire (null=False). la base de donnee le garrantie

* En creant une cle unique entre une offre et un etudiant, la base de donnee garrantie cette regle pour eviter les doublons

* Promotion: un nombre , elle est stockée comme une année numérique afin de pouvoir facilement calculer des statistiques de placement par promotion

* statut d'une candidature: une liste fermee pour éviter les fautes de frappe

La responssable des stages dit On ne perd jamais l’historique d’un stage. 

Donc on évite CASCADE pour les relations historiques importantes.



* On ne peut pas supprimer un étudiant qui a candidaté à une offre, afin de conserver l’historique des candidatures.
* On ne peut pas supprimer une offre pour laquelle un étudiant a candidaté, afin de conserver l’historique des candidatures.
* On ne peut pas supprimer une candidature qui est associée à un stage, afin de conserver l’historique du stage.
* On ne peut pas supprimer une entreprise qui possède au moins un tuteur ou qui a publié des offres, afin de conserver l’historique.
* On ne peut pas supprimer un tuteur qui suit un stage, afin de conserver l’historique du stage.
* On ne peut pas supprimer un enseignant référent qui suit un stage, afin de conserver l’historique du stage.

