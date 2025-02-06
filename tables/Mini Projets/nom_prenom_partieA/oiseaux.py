# Importation de la bibliothèque CSV pour manipuler les fichiers .csv
import csv

# Dictionnaire pour stocker les données des fichiers CSV
# Chaque clé est un numéro de table, et chaque valeur est une liste de dictionnaires représentant les lignes du fichier
tables = {}

# Lecture des fichiers CSV et stockage dans le dictionnaire
for nb, name in enumerate([
        "Oiseaux1",
        "Oiseaux2",
        "couleur2",
    ],
    start = 1
):
    # Ouverture du fichier CSV en mode lecture
    with open(
        file     = f"{name}.csv",
        mode     = "r",
        encoding = "utf-8-sig"
    ) as f:
        # Lecture du fichier CSV et stockage des données dans le dictionnaire
        tables[nb] = list(
            csv.DictReader(f, delimiter = ",")
        )

# Fusion des données des tables Oiseaux1 et Oiseaux2
# Création d'une nouvelle table qui combine les deux
table12 = tables[1] + tables[2]

# Écriture des données fusionnées dans un nouveau fichier CSV
with open("Oiseaux3.csv","w") as sortie:
    # Création d'un objet DictWriter pour écrire les données dans le fichier
    objet = csv.DictWriter(sortie, ['nom', 'couleur1'])
    objet.writeheader()  # Écriture de l'en-tête
    objet.writerows(table12)  # Écriture des lignes fusionnées

# Fonction pour fusionner deux lignes de données d'oiseaux
def fusionOiseau(ligneA, ligneB):
    '''In : ligneA la table 1 et ligneB de la table 4
    Out : le dictionnaire fusion'''
    return {
        "nom"     : ligneA["nom"],
        "couleur1": ligneA["couleur1"],
        "couleur2": ligneB["couleur2"]
    }

# Liste pour stocker les résultats de la jointure
jointureOIseau=[]

# Jointure des données entre table12 et la table couleur2
for ligneA in table12:
    for ligneB in tables[3]:
        # Vérification si le nom des oiseaux correspond
        if ligneA["nom"] == ligneB["nom"]:
            # Ajout de la ligne fusionnée à la liste des résultats
            jointureOIseau.append(fusionOiseau(ligneA, ligneB))

# Écriture des résultats de la jointure dans un fichier CSV
with open("bilan_oiseaux.csv","w")as sortie:
    # Création d'un objet DictWriter pour écrire les résultats
    objet=csv.DictWriter(sortie, ['nom', 'couleur1', 'couleur2'])
    objet.writeheader()  # Écriture de l'en-tête
    objet.writerows(jointureOIseau)  # Écriture des résultats de la jointure

# Afficher les résultats de la fusion
print("==========jointure==========")
print(jointureOIseau)
print()