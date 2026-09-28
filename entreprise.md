# Specification

## 1. Champs qui identifie une entreprise

**Nom + ville identifie une entreprise sans ambiguïté**

Non. L'agence Ecobank à Sokodé et l'agence Ecobank à Lomé sont 2 entreprises différentes.

Car les deux banques n'ont pas les mêmes offres de stages, un stagiaire est physiquement affecté à une zone géographique précise, et les contacts locaux ou les opportunités diffèrent d'une ville à l'autre.

## 2. Email

Pour email il faut utiliser le type **EmailField()**. Il faut l'utiliser plutôt qu'un TextField car cela permet à Django de vérifier si le champ saisi a une structure d'adresse e-mail valide.

## 3. Secteur d'activité

Il faut retenir une **liste de valeurs imposée** (via une énumération).

### Liste de valeurs imposée

- **Coût aujourd'hui :** Demande un effort technique initial (création d'une énumération) et un travail de définition des secteurs avec le secrétariat, tout en bloquant l'utilisateur si un nouveau secteur apparaît.

- **Coût dans trois mois :** Faible, car elle garantit des données propres et standardisées.

### Le texte libre (Option rejetée)

- **Coût aujourd'hui :** Zéro effort de développement initial car le champ accepte n'importe quelle saisie de l'utilisateur sans configuration préalable.

- **Coût dans trois mois :** Élevé, car les fautes et les différentes écritures rendront les recherches et les statistiques difficiles.

## 4. Affichage

Elle parle de l'expérience utilisateur et de l'**affichage des données** (comme la surcharge de la méthode `__str__` en programmation). Le secrétariat exprime le besoin visuel d'un libellé clair et immédiatement reconnaissable à l'écran.

# 3.2 Migrer

### a.

Elle s'appelle **"nom_ville"**.

### b.

C'est la colonne **id**. Django l’ajoute automatiquement comme clé primaire pour identifier chaque entreprise.

### c.

Après avoir changé `max_length` et lancé `makemigrations`, Django crée un nouveau fichier de migration. Il y a donc maintenant **4 fichiers de migration**. Pour revenir en arrière, il faut supprimer la nouvelle migration si elle n’a pas encore été appliquée.

# 4. L'administration

### a.

En validant.

### b.

Oui.

# 6. Restitution

### 1.

`uv python pin 3.14`
`uv sync`
c'est `uv sync`, car elle utilise `uv.lock` qui contient les versions précises des dépendances.

### 2.

Le fichier de migration décide de la forme de la table au moment où Django l’applique à la base de données.

### 3.

Erreur 1 : URL incorrecte

Ce qui m'a mis sur la voie : la liste des URL que Django avait essayées.

Erreur 2 : template introuvable

Ce qui m'a mis sur la voie : le nom du template recherché.