import csv
import pandas as pd

# 1. Le problème 
print("======1. Le problème======")
def csv1(file_path, separator):
    import pandas as pd
    tab = pd.read_csv(file_path, sep=separator)
    return tab

tab = csv1('projet csv\exemple.csv', ',')
print(tab)
print()

# Questions:
# 1. Expliquer ce qu’est un fichier csv
# Un fichier csv est un fichier texte qui contient des données tabulaires.
# 2. En vous appuyant sur l’exemple proposé et à la variable tab obtenue, comment accéder aux descripteurs du fichier csv ?
# On utilise la fonction csv.reader() ou avec pandas on utilise la fonction pd.read_csv()
# 3. Comment accéder à l’année de la ligne n°4 (ce numéro de ligne fait référence à celui du tableur ou de l’éditeur de texte [reponse : 2021 ]) ?
# On accede en faisant tab[3][1]
# 4. Comment accéder au prix de la ligne n°4 [reponse : 56.3 ], au format numérique (float) ?
# On accede en faisant float(tab[3][2])

# 2 Découpage du projet
print("======2. Découpage du projet======")
print()
# 2.1 Fonction tranche
print("====2.1 Fonction tranche====")
def tranche(chaine, d, f):
    return chaine[d:f]

print(tranche("bonjour à vous tous", 10, 14))
print()

# 2.2 Fonction indices
print("====2.2 Fonction indices====")

def indices(chaine, c):
    return [i for i, x in enumerate(chaine) if x == c]

print(indices("bonjour à vous tous", 'o'))
print()

# 2.3 Fonction partage
print("====2.3 Fonction partage====")

def partage(chaine, car):
    return chaine.split(car)

print(partage("bonjour à vous tous", 'o'))
print( partage(",chp2,chp3,,chp5,,,", ','))
print()