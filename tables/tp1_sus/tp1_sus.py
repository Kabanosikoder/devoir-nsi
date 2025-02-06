# Partie 1: Partie 1 : Création de Tables
print("======Partie 1======")
print()
# Exercice 1 : Création d’une table simple
print("===Excercice 1===")

table1 = [
[" Alice ", 1990 , " Lyon "] ,
[" Bob", 1985 , " Marseille "] ,
[" Charlie ", 2000 , " Lille "]
]
print (table1 [1][2])

# Exercice 2 : Utilisation de dictionnaires
print("===Excercice 2===")

table2 = [
    {"Nom": "Alice", "Année": 1990, "Ville": "Lyon"},
    {"Nom": "Bob", "Année": 1985, "Ville": "Marseille"},
    {"Nom": "Charlie", "Année": 2000, "Ville": "Lille"}
]

# Votre code ici pour afficher l'année de Charlie
print(table2[2]["Année"])

# Partie 2 : Importation d’un Fichier CSV
print("======Partie 2======")
print()
# Exercice 1 : Lecture avec csv.reader
print("===Excercice 1===")
import csv

with open('data.csv', 'r') as f:
    table1 = list(csv.reader(f))
    print(table1)
print()
# Exercice 2 : Lecture avec csv.DictReader
print("===Excercice 2===")

with open ("data.csv", "r") as f :
    table2 = list (csv.DictReader (f) )

for row in table2 :
    print ( row ['Ville'])
print()
# Partie 3 : Traitement des Données
print("======Partie 3======")
print()
# Exercice 1 : Conversion des types
print("===Excercice 1===")

for row in table2:
    row['Year'] = int(row['Year'])  # Use the key as it appears in the output

somme_annees = sum(row['Year'] for row in table2)
print("Somme des années :", somme_annees)
print()
# Exercice 2 : Recherche
print("===Excercice 2===")
def rechercher_nom (table, nom) :
    for row in table :
        if row ['Nom'] == nom :
            return row
    return None

resultat = rechercher_nom (table2, 'Alice')
print (resultat)
print()

#Questions Ouvertes
# — Pourquoi est-il préférable d’utiliser un index numérique plutôt qu’un nom comme clé principale ?
# Il est preferable d'utiliserun index numérique pour faciliter la recherche et pour garder la simplicité du programme.
# — Quels sont les avantages de csv.DictReader par rapport à csv.reader ?
# Les avantages de csv.DictReader sont : 
# - plus simple d'utiliser, 
# - plus facile de lire et plus rapide
# - plus rapide à l'écriture
