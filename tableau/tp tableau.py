# TP:Manipulation des Tableaux

# Niveau Avancé

# Exercice 6: Voici un algorithme pour créer une matrice carrée (n x n) où chaque cellule
# contient le produit de ses indices. Traduisez cet algorithme en une fonction Python

print("===== Exercice 6 ======")
def create_product_matrix(n):
    matrice = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = i * j
    return matrice

# test
n = 5
matrix = create_product_matrix(n)
for line in matrix:
    print(line)
print("")

# Exercice 7: Voici un algorithme qui renvoie le nombre d'occurrences d'un élément donné
# dans une liste. Traduisez cet algorithme en une fonction Python.

print("===== Exercice 7 =====")

def count_occurrences(liste, element):
    compteur = 0
    for e in liste:
        if e == element:
            compteur += 1
    return compteur

# test
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5
occurrences = count_occurrences(liste, element)
print(f"Le nombre d'occurrences de {element} dans la liste est: {occurrences}")
print("")

# Niveau Intermédiaire
# Exercice 4: Complétez la fonction filter_even(liste) ci-dessous pour qu'elle renvoie une
# nouvelle liste qui contient seulement les nombres pairs de liste
print("===== Exercice 4 =====")

def filter_even(liste):
    return [x for x in liste if x % 2 == 0]

# test
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter_even(liste)
print(even_list)
print("")

# Exercice 5: Complétez la fonction create_matrix(m, n) ci-dessous pour qu'elle crée et
# renvoie une matrice de taille m x n remplie de zéros.
print("===== Exercice 5 =====")

def create_matrix(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]

# test
m = 5
n = 5
matrix = create_matrix(m, n)
for line in matrix:
    print(line)
print("")


# Niveau Débutant

# Exercice 1: Écrivez une fonction create_list(n) qui crée et renvoie une liste de nombres
# entiers de 1 à n.
print("===== Exercice 1 =====")

def create_list(n):
    return list(range(1, n + 1))

# test
n = 8
liste = create_list(n)
print(liste)
print("")

# Exercice 2: Écrivez une fonction reverse_list(liste) qui renvoie la liste inverse de liste.
print("===== Exercice 2 =====")

def reverse_list(liste):
    return liste[::-1]

# test
liste = [1, 2, 3, 4, 5]
reverse_liste = reverse_list(liste)
print(reverse_liste)
print("")

# Exercice 3: Écrivez une fonction find_sum(liste) qui calcule et renvoie la somme des éléments de liste.
print("===== Exercice 3 =====")

def find_sum(liste):
    return sum(liste)

# test  
liste = [1, 2, 3, 4, 5]
somme = find_sum(liste)
print(somme)
print("")