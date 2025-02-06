import csv
import pandas as pd   # do 'pip install pandas' in your terminal before before running the program so it can run
# TP3-4: Traitement de Données en Table - Fusion de Tables
# 2 Chargement des Données
print("======Chargement des Donnees======")

elements = pd.read_csv('elements.csv')
familles = pd.read_csv('familles.csv')

print(f"Descripteurs des éléments : {elements.columns}")
print(f"Descripteurs des familles : {familles.columns}")
print()

# 3 Affichage des Données
print("======Affichage des Donnees======")
def affichage(table):
    if len(table) == 0:
        print("Table vide")
        return
    df = pd.DataFrame(table)
    print(df)

affichage(elements)
affichage(familles)
print()

# 4 Fusion des Tables
table_fusionnee = pd.merge(elements, familles, on="Symbole")

# 5 Affichage de la Table Fusionnée
print("======Affichage de la Table Fusionnée======")
affichage(table_fusionnee)
print()