# TD Exercices Tableaux
# Exercice 1: Création et accès aux éléments d'une liste
fruits = ['Pomme', 'Banane', 'Mangue','Citron','Orange']
print(fruits[0])
print(fruits[4])
fruits[1] = 'Ananas'
print(fruits)

# Exercice 2: Méthode append()
fruits.append('Kiwi')
print(fruits)

# Exercice 3: Création d'une liste par compréhension
carres = [i*i for i in range(1, 11)]
print(carres)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercice 4: Création d'un tableau de tableaux (matrice)
# 1. Créez une matrice 3x3 contenant les nombres de 1 à 9.
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 2. Accédez à l'élément en deuxième ligne et troisième colonne.
print(matrice[1][2])
# 3. Modifiez cet élément pour 0.
matrice[1][2] = 0

# Exercice 5: Représentation d'une grille de jeu
# Représentez la grille du jeu de Morpion donnée dans l'exercice du cours comme une liste de listes en Python.
morpion_liste = [
[0, 0, 0], 
[0, 0, 0], 
[0, 0, 0]
]
# 2. Écrivez une fonction Python pour afficher l'état de la grille ligne par ligne.
for i in range(3):
    for j in range(3):
        print(morpion_liste[i][j], end=" ")
    print()

# Exercice 6: Itérations sur les listes
# 1. Écrivez un programme Python pour afficher tous les éléments de la liste 'fruits' un par un en utilisant une boucle for.
for fruit in fruits:
    print(fruit)

print()

# 2. Écrivez un autre programme Python pour faire la même chose, mais cette fois en utilisant l'index de chaque élément.
for i in range(len(fruits)):
    print(fruits[i])