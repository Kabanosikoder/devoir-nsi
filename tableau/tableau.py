from random import randint

# Cours sur les tableaux
# 2.1 Création d’un tableau (liste-Python)
print("2.1 Création d’un tableau (liste-Python)")
liste = ['Henri','Louis','ELISABETH']
print(liste)
init = [0] * 5
print(init)
# [0, 0, 0, 0, 0]

# 2.2 Accès à un élément
print("2.2 Accès à un élément")
liste[0]
print(liste[0])
# 'Henri'
print(liste[1])
# 'Louis'
print(liste[2])
# 'ELISABETH'

# 2.3 Modification d’un élément
print("2.3 Modification d’un élément")
liste[2] = 'Elisabeth'
print(liste)
# ['Henri', 'Louis', 'Elisabeth']

# 2.4 Ajout d’un élément
print("2.4 Ajout d’un élément")
liste.append('Cesar')
print(liste)
# ['Henri', 'Louis', 'Elisabeth', 'Cesar']

# 3 Création d’un tableau par compréhension
print("3 Création d’un tableau par compréhension")
n = 10
liste = [i for i in range(1, n+1) if i % 2 == 0]
# pour n = 10 : [2, 4, 6, 8, 10]
print(liste)

tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
tranche = [tab[i] for i in range(2, 5)]
print(tranche)
# ['c', 'd', 'e']

# 4 Représentation de matrices : tableau de tableaux
print("4 Représentation de matrices : tableau de tableaux")
# 4.1 Principe
print("4.1 Principe")
matrice = [[6, 3, 1, 1, 4], # Remarque : Pour plus de lisibilité, on peut écrire la construction du tableau de tableaux sur plusieurs lignes
[4, 5, 2, 2, 4],
[6, 1, 1, 2, 5]
]
## chaque élément du tableau est aussi un tableau !
matrice[0]
print(matrice[0])
# [6, 3, 1, 1, 4]
matrice[1]
print(matrice[1])
# [4, 5, 2, 2, 4]
matrice[2]
print(matrice[2])
# [6, 1, 1, 2, 5]

# Exemple :
# Le chiffre 3 souligné de l’exemple précédent est accessible par matrice[0][1]:
print("Exemple :")

matrice[0][1]   # rappel : matrice[0] vaut [6, 3, 1, 1, 4]
print(matrice[0][1])
# 3

# Exemple 2 : création d’une matrice de nombres aléatoires entre 1 et 6 « en compréhension » :
m, n = 3, 5 # 3 lignes de 5 colonnes
matrice = [[randint(1, 6) for i in range(n)] for j in range(m)]
print(matrice)

# Excercices:
print("Excercice:")
# 1. jeu du Morpion, la liste du jeu
morpion_liste = [
[0, 1, 0], 
[2, 1, 0], 
[2, 0, 0]
]

# 2. Comment acceder a la case du coin inferieur gauche ?
print(morpion_liste[2][0]) # 2

# 3. Ecrire un code Python qui affiche ligne apres ligne l'etat de la grille.
# Par exemple, pour la grille donne precedemment, l'affichage doit etre :
# 0 1 0
# 2 1 0
# 2 0 0
for i in range(3):
    for j in range(3):
        print(morpion_liste[i][j], end=" ")
    print()

# 5 Itérations sur les tableaux
print("5 Itérations sur les tableaux")
# 5.1 Parcours par élément
print("5.1 Parcours par élément")
# Parcours par élément
for element in tab:
    print(element)

# 5.2 Parcours par indice
print("5.2 Parcours par indice")
for i in range(len(tab)):
    print(tab[i])