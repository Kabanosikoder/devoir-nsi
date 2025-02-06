# Exemple 1
# Represantion sous forme de tableau doublement indexé
table1 = [["Andrew", "2002", "Caen"],
["Steven", "2002", "Londres"],
["Walter", "2007", "Paris"]
]

# Representation sous forme de tableau de p-uplets nommes
table2 = [{"Nom" :"Andrew", "Année": "2002", "Ville": "Caen"},
{"Nom" :"Steven", "Année": "2002", "Ville": "Londres"},
]

print("Ville de Andrew (tableau doublement indexé): ", table1[0][2])
print("Ville de Andrew (tableau de p-uplets): ", table2[0]["Ville"])

# Exemple 2:
import csv

############ fonction csv.reader ############
with open('exemple.csv', 'r') as f:
    table1 = list(csv.reader(f, delimiter=','))

############ fonction csv.DictReader ############
with open('exemple.csv', 'r') as f:
    table2 = list(csv.DictReader(f, delimiter=','))