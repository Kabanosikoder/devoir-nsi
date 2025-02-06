import csv

# Étape 1 : Importer les fichiers CSV et créer les tables de dictionnaires
prenoms2003 = []
prenoms2004 = []

with open('prenoms2003.csv', mode='r', encoding='utf-8-sig') as f2003:
    reader = csv.DictReader(f2003)
    for row in reader:
        prenoms2003.append(row)

with open('prenoms2004.csv', mode='r', encoding='utf-8-sig') as f2004:
    reader = csv.DictReader(f2004)
    for row in reader:
        prenoms2004.append(row)

# Étape 2 : Effectuer la réunion des deux tables
# On peut simplement concaténer les deux listes
prenoms_combines = prenoms2003 + prenoms2004

# Étape 3 : Exporter les données obtenues dans un fichier CSV
with open('prenoms2003-2004.csv', mode='w', newline='', encoding='utf-8-sig') as sortie:
    fieldnames = prenoms_combines[0].keys()  # Utiliser les clés du premier dictionnaire comme en-tête
    writer = csv.DictWriter(sortie, fieldnames=fieldnames)
    writer.writeheader()  # Écrire l'en-tête
    writer.writerows(prenoms_combines)  # Écrire les lignes combinées

print("Les données ont été exportées avec succès dans 'prenoms2003-2004.csv'.")
print("==========prenoms==========")
print(prenoms_combines)
print("==========end==========")