# Exercice 1 : Chercher la position
tab1 = [10, 20, 30, 40, 50]
e1 = 30

def cherche_position(tab,e):
    for i in range(0, len(tab)):
        if tab[i] == e:
            return i
    return -1

print(cherche_position(tab1, e1))
# 2

# Exercice 2 : Trouver le minimum
tab2 = [15, 25, 5, 30, 20]

def minimum(tab):
    min = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < min:
            min = tab[i]
    return min

print(minimum(tab2))
# 5

# Exercice 3 : Calculer la moyenne
tab3 = [20, 30, 40, 50, 60]

def moyenne(tab):
    somme = 0
    for nb in tab:
        somme = somme + nb
    return somme / len(tab)

print(moyenne(tab3))
# 40.0

# Exercice 4 : Algorithme quadratique
tab4 = [1, 2, 3, 2, 1]

def quad(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if tab[i] == tab[j]:
                return True
    return False

print(quad(tab4))
# True