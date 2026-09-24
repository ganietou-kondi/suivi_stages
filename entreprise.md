## Specification
1- Champs qui identifie une entreprise: nom, ville identifie une entreprise sans ambiguite 

Non. l'agence Ecobank à Sokodé et l'agence Ecobank à Lomé sont 2 entreprise differentes.
car les deux banque n'ont pas las meme offres de stages, un stagiaire est physiquement affecté à une zone géographique précise, et les contacts locaux ou les opportunités diffèrent d'une ville à l'autre.

2- Pour email il faut utiliser le type EmailField().  il faut l'utiliser plutot qu'un textfield car cella permet a django de verifier si le champ saisie a une structure d'addresse e-mail valide 


3- Secteur d'activite
Il faut retenir une **liste de valeurs imposée** (via une énumération). 
**liste de valeurs imposée**
* Coût aujourd'hui : Demande un effort technique initial (création d'une énumération) et un travail de définition des secteurs avec le secrétariat, tout en bloquant l'utilisateur si un nouveau secteur apparaît.
*   Coût dans trois mois : Extrêmement faible, car elle garantit des données parfaitement propres et standardisées, permettant de générer des rapports et des statistiques fiables de manière 100 % automatique.


**Le texte libre (Option rejetée)**
*   Coût aujourd'hui : Zéro effort de développement initial car le champ accepte n'importe quelle saisie de l'utilisateur sans configuration préalable.
*   Coût dans trois mois : Très élevé, car la prolifération de fautes de frappe et de variantes (ex: "Informatique", "informatique", "IT") rendra les filtres de recherche inutilisables et l'extraction de statistiques impossible sans un nettoyage de données manuel long et coûteux.

4- Elle parle de l'expérience utilisateur et de l'**affichage des données** (comme la surcharge de la méthode `__str__` en programmation ). Le secrétariat exprime le besoin visuel d'un libellé clair et immédiatement reconnaissable à l'écran.


