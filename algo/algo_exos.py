# Exercice 1: Chercher la position d'un élément dans un tableau
def cherche_position(tab,e):
    for i in range(0, len(tab)):
        if tab[i] == e:
            return i
    return -1

# Exercice 2: Chercher la position d'un élément dans un tableau
def minimum(tab):
    min = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < min:
            min = tab[i]
    return min

# Exercice 3: Calculer la moyenne d'un tableau
def moyenne(tab):
    somme = 0
    for nb in tab:
        somme = somme + nb
    return somme / len(tab)

# Exercice 4: Un exemple d'algorithme de coût quadratique
def quadratique(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if tab[i] == tab[j]:
                return True
    return False
    