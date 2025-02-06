import csv

# Partie 1:
print("======Partie 1======")
print()
# Excercice 1:Création d’un fichier texte
print("===Excercice 1===")

# ecriture dans un fichier texte
with open('monfichier.txt', 'w') as f:
    f.write("Première ligne du fichier\n")
    f.write("Deuxième ligne du fichier\n")
    f.write("Troisième ligne du fichier\n")

# Lecture ligne par ligne
with open('monfichier.txt', 'r') as f:
    for line in f:
        print(line.strip())

print()
# Exercice 2: Analyse d’un fichier texte existant
print("===Excercice 2===")
# Lecture et analyse du fichier
with open('fichier-test.txt', 'r') as f:
    lignes = f.readlines()
    print(f"Nombre de lignes : {len(lignes)}")
    print(f"Dernière ligne : {lignes[-1].strip()}")

print()
# Partie 2 : Manipulation des données tabulaires
print("======Partie 2======")
print()
# Exercice 1 : Création et lecture d’un fichier CSV
print("===Excercice 1===")
with open('data.csv', 'r') as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)

print()

# Exercice 2 : Analyse avancée d’un fichier CSV
print("===Excercice 2===")
with open('data.csv', 'r') as f:
    lecteur = csv.DictReader(f)
    ages = [int(row['Age']) for row in lecteur]

age_moyen = sum(ages) / len(ages) if ages else 0 
print(f"Age moyen : {age_moyen}")
print()

# Questions ouvertes
print("======Questions ouvertes======")

# 1. Pourquoi est-il important de fermer un fichier après l’avoir utilisé ?
# Pour ne pas consommer de ressources inutiles.

# 2. Quels sont les avantages d’utiliser le module csv.DictReader ?
# On peut lire directement des colonnes nommées.

#  3. Comment gérer les erreurs potentielles liées à l’ouverture ou la lecture d’un fichier inexistant ?
# On utilise try: et except: en python pour gérer les erreurs.