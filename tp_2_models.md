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

# 3
* a- Il ya 10 table qui ont ete creer 
Stage_etudiant_competance et Stage_offre_competance je ne les ai pas ecrite 
Django les crée automatiquement pour gérer tes relations ManyToMany.
* b- Non il n'y a pas de table personne, Oui c'est cherant avce mon choix de la partie 2 

* c- CREATE TABLE "new__stages_candidature" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "statut" varchar(150) NOT NULL, "date_depot" date NOT NULL, "etudiant_id" bigint NOT NULL REFERENCES "stages_etudiant" ("id") DEFERRABLE INITIALLY DEFERRED, "offre_id" bigint NOT NULL REFERENCES "stages_offre" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "offre_etudiant" UNIQUE ("etudiant_id", "offre_id"));

Elle apparait sous forme de contrainte d'unicite

* d- Les règles PROTECT définies dans les modèles sont gérées par Django lors des suppressions effectuées avec l'ORM. Elles n'apparaissent pas sous la forme ON DELETE PROTECT dans le SQL généré. Une suppression effectuée directement en SQL ne passe donc pas par la vérification PROTECT de Django ; elle est alors soumise aux contraintes réellement présentes dans la base de données.


# 4

a- Cannot delete entreprise
Deleting the selected entreprise would require deleting the following protected related objects:
    Offre: Offre object (1)

Oui c'est ce qu'elle voulais

b- Django aurait autorisé la suppression de l'entreprise.
Et il aurait également supprimé automatiquement les offres liées à cette entreprise, ainsi que les autres objets dépendants selon les relations CASCADE.