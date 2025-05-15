# ========== 1 Recherche d’un élément ==========

def cherche1(tab, e):
    """ Recherche si l'élément e est présente dans le tableau tab """
    for element in tab:                 # Parcourt chaque élément de la liste tab
        if element == e:                # Vérifie si l'élément courant est égal à e
            return True                 # Si oui, renvoie True et arrête la fonction
    return False                        # Si aucun élément n'est égal à e, renvoie False

# Exemple d'application
tab = [2, 4, 6, 8, 10]
print(cherche1(tab, 6))  # Affiche True car 6 est dans la liste
print(cherche1(tab, 7))  # Affiche False car 7 n'est pas dans la liste

# Coût de l'algorithme
# Complexité en temps : O(n), où n est la taille de la liste (il faut parfois tout regarder)
# Complexité en espace : O(1), car on n'utilise pas de mémoire supplémentaire

# Explication ligne par ligne de la fonction cherche2

def cherche2(tab, e):
    # """ Recherche si l'élément e est présente dans le tableau tab """
    for i in range(len(tab)):              # Parcourt tous les indices de la liste tab
        if tab[i] == e:                    # Vérifie si l'élément à l'indice i est égal à e
            return True                    # Si oui, renvoie True et arrête la fonction
    return False                           # Si la boucle finit sans trouver e, renvoie False

# Exemple d'application
tab = [2, 4, 6, 8, 10]
print(cherche2(tab, 6))  # Affiche True car 6 est dans la liste
print(cherche2(tab, 7))  # Affiche False car 7 n'est pas dans la liste

# Coût de l'algorithme
# Complexité en temps : O(n), où n est la taille de la liste (parfois il faut tout regarder)
# Complexité en espace : O(1), car on n'utilise pas de mémoire supplémentaire

def cherche_position(tab, e):
    # """ Renvoie l'indice de 1ère occurrence de l'élément e s'il est présent dans le tableau tab, ou -1 dans le cas contraire """
    for i in range(len(tab)):                 # Parcourt tous les indices de la liste tab
        if tab[i] == e:                       # Si l'élément à l'indice i est égal à e
            return i                          # Renvoie l'indice i (position trouvée)
    return -1                                 # Si e n'est pas trouvé, renvoie -1

# Exemple d'application
tab = [2, 4, 6, 8, 10]
print(cherche_position(tab, 6))  # Affiche 2 car 6 est à l'indice 2
print(cherche_position(tab, 7))  # Affiche -1 car 7 n'est pas dans la liste

# ========== 2 Recherche d’un extremum ==========

def maximum(tab):
    """ Recherche la valeur maximum dans le tableau tab """
    # préconditions : tableau non vide,
    # contenant des éléments tous comparables entre eux
    maxi = tab[0]                  # valeur maxi par défaut (le premier élément)
    for i in range(1, len(tab)):   # parcours du tableau à partir du 2ème élément
        if tab[i] > maxi:          # si l'élément courant est plus grand que maxi
            maxi = tab[i]          # on met à jour maxi
    return maxi                    # on retourne la plus grande valeur trouvée

# Exemple d'application
tab = [2, 4, 6, 8, 10]
print(maximum(tab))  # Affiche 10 car c'est le plus grand élément

# Coût de l'algorithme
# Complexité en temps : O(n), où n est la taille du tableau (on regarde tous les éléments)
# Complexité en espace : O(1), car on n'utilise qu'une variable supplémentaire

def minimum(tab):
    """ Recherche la valeur minimum dans le tableau tab """
    # préconditions : tableau non vide,
    # contenant des éléments tous comparables entre eux
    mini = tab[0]                  # valeur mini par défaut (le premier élément)
    for i in range(1, len(tab)):   # parcours du tableau à partir du 2ème élément
        if tab[i] < mini:          # si l'élément courant est plus petit que mini
            mini = tab[i]          # on met à jour mini
    return mini                    # on retourne la plus petite valeur trouvée

# Exemple d'application
tab = [2, 4, 6, 8, 10]
print(minimum(tab))  # Affiche 2 car c'est le plus petit élément

# Coût de l'algorithme
# Complexité en temps : O(n), où n est la taille du tableau (on regarde tous les éléments)
# Complexité en espace : O(1), car on n'utilise qu'une variable supplémentaire

# ========== 3 Calcul d’une moyenne =========

def moyenne(tab):
    """ Calcule la moyenne des valeurs dans le tableau tab """
    # précondition : le tableau contient des valeurs numériques
    somme = 0                       # somme des valeurs du tableau (nulle a priori)
    for nb in tab:                  # parcours par élément
        somme = somme + nb
    # la moyenne est la somme divisée par le nb de valeurs
    return somme / len(tab)

# Exemple d'application
tab = [2, 4, 6, 8, 10]
print(moyenne(tab))  # Affiche 6.0 car (2+4+6+8+10)/5 = 30/5 = 6.0

# Coût de l'algorithme
# Complexité en temps : O(n), où n est la taille du tableau (on additionne tous les éléments)
# Complexité en espace : O(1), car on utilise seulement une variable supplémentaire