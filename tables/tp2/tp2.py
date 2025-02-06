import csv
from copy import deepcopy

# Partie 1
print("======Partie 1======")
# Excercice 1a
print("===Excercice 1a===")

# 1) Import des données

with open('region2019.csv', 'r') as f:
    regions = list(csv.reader(f))

# 2) Affichage des descripteurs et du 1er enregistrement
print(regions[0])  # Liste des descripteurs
print(regions[1])  # Premier enregistrement

# 3) Fonction pour trouver le code d’une région
def code_region(table, nom_region):
    for row in table[1:]:
        if row[3].lower() == nom_region.lower():
            return row[0]
    return None

# 4) Recherche du code pour Normandie
print(code_region(regions, 'Normandie'))
print()
# Exercice 1b : Recherche avec un tableau de p-uplets nommes
print("===Excercice 1b===")

# 1) Import des données
import csv

with open('region2019.csv', 'r') as f:
    regions = list(csv.DictReader(f))

# 2) Affichage du 1er enregistrement
print(regions[0])

# 3) Fonction pour trouver le code d’une région
def code_region(table, nom_region):
    for row in table:
        if row['ncc'].lower() == nom_region.lower():
            return row['reg']
    return None

# 4) Recherche du code pour Normandie
print(code_region(regions, 'Normandie'))
print()

# Partie 2 : Recherche avancee
print("==========Partie 2==========")
print()
# Excercice 2
print("===Excercice 2===")
# 1) Import des données

with open('departement2019.csv', 'r', encoding='utf-8') as f:
    departements = list(csv.DictReader(f))

# 2) Affichage du 1er département
print(departements[0])

# 3) Fonction pour les départements d’une région
def departements_region(table, code_region):
    return [row['dep'] for row in table if row['reg'] == code_region]

# 4) Départements de Normandie
print(departements_region(departements, '28'))  # Code de la Normandie

# Partie 3 : Coherence des données
print("==========Partie 3==========")
print()
# Exercice 4 : Rendre les données coherentes
print("===Excercice 4===")

# 1) Import des données
with open('enquete.csv', 'r', encoding='utf-8') as f:
    data = list(csv.reader(f))

# 2) Affichage des 10 premières personnes
for row in data[:10]:
    print(row[0], row[2])

# 3) Correction des sommes
data_OK = deepcopy(data)
for row in data_OK:
    row[2] = row[2].replace(',', '.')
    if row[2].startswith('$'):
        row[2] = row[2][1:]
    elif row[2].endswith('$'):
        row[2] = row[2][:-1]

print(data_OK[:10])

# FIN