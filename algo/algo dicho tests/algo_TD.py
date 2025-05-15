# Excercices Dichotomie

# Exercice 1: Comprendre l'algo
print("==== Exercice 1 =====")
print()
# Considerez le tableau suivant qui est trié dans l'ordre croissant: [1,3,4,5,7,8,12,13,14,15,16,18,19,20]
# Utilisez l'algo de dichotomie pour trouver les valeurs suivantes et indiquez a chaque etape le sous-tableau sur lequel vs cherchez

def recherche_dichotomique(tab, val):
    gauche = 0
    droite = len(tab) - 1
    etape = 1
    
    print(f"Recherche de {val} dans le tableau : {tab}")
    
    try:
        # Essayer de convertir la valeur en entier
        val = int(val)
    except (ValueError, TypeError):
        print(f"Erreur : '{val}' n'est pas un nombre valide")
        return -1
        
    gauche = 0
    droite = len(tab) - 1
    etape = 1
    
    print(f"\nRecherche de {val} dans le tableau : {tab}")
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        sous_tableau = tab[gauche:droite+1]
        print(f"\nÉtape {etape}:")
        print(f"  Sous-tableau: {sous_tableau}")
        print(f"  Milieu: {tab[milieu]} (indice {milieu})")
        
        if tab[milieu] == val:
            print(f"  Trouvé {val} à l'indice {milieu}!")
            return milieu
        elif tab[milieu] < val:
            print(f"  {tab[milieu]} < {val}, on cherche à droite")
            gauche = milieu + 1
        else:
            print(f"  {tab[milieu]} > {val}, on cherche à gauche")
            droite = milieu - 1
        etape += 1
    
    print(f"\n{val} n'est pas dans le tableau")
    return -1

# Tests, avec des valeurs hors la liste et des valeurs non numériques
print("==== Pour 12 ====")
print()
print(recherche_dichotomique([1,3,4,5,7,8,12,13,14,15,16,18,19,20], 12))
print()
print("==== Pour 1 ====")
print()
print(recherche_dichotomique([1,3,4,5,7,8,12,13,14,15,16,18,19,20], 1))
print()
print("==== Pour 20 ====")
print()
print(recherche_dichotomique([1,3,4,5,7,8,12,13,14,15,16,18,19,20], 20))
print()
print("==== Pour 21 ====")
print()
print(recherche_dichotomique([1,3,4,5,7,8,12,13,14,15,16,18,19,20], 21))
print()
print("==== Pour a ====")
print()
print(recherche_dichotomique([1,3,4,5,7,8,12,13,14,15,16,18,19,20], "a"))
print()
print("==== Pour -6 ====")
print()
print(recherche_dichotomique([1,3,4,5,7,8,12,13,14,15,16,18,19,20], -6))
print()
print()

print("==== Exercice 2 ====")
# Modifications de l'algo
# Modifiez l'implimentation Python de l'algo de recherche dichotomique pour qu'elle renvoie non seulement l'indice ou la valeur est trouvée, mais aussi
# le nombre d'itérations necessaires pour la trouver. Testez votre nvelle fonction sur le tableau [2,4,6,8,10,12,14,16,18,20] avec les valeurs 6 et 19
print("==== Pour 6 ====")
print()
print(recherche_dichotomique([2,4,6,8,10,12,14,16,18,20], 6))
print()
print("==== Pour 19 ====")
print()
print(recherche_dichotomique([2,4,6,8,10,12,14,16,18,20], 19))
print()

print("==== Exercice 3 ====")
# Comprendre les propriétés de l'algo
print()

# Expliquez pourquoi il est important que le tableau soit trié pour utiliser l'algo de recherche dicho. Que passerait-il si le tableau n'était pas trié ?
# Il est important que le tableau soit trié pour utiliser l'algo de recherche dicho car 
# l'algo de recherche dicho utilise la division par 2 pour trouver l'element.
# Donc si le tableau n'était pas trié, l'algo ne fonctionnerait pas car il ne saurait pas trouver l'element.

print("==== Exercice 4 ====")
# Analiser la complexité
print()

# On dit que la complexité de l'algo de la recherche dicho est en log2(N). Qu'est ce que celq signifie? 
# Expliquez pourquoi cela est vrai en utilisant vos propres mots.
# log₂(N) représente le nombre de fois où on peut diviser N par 2 avant d'arriver à 1.

# log₂(8) = 3 car 8 ÷ 2 ÷ 2 ÷ 2 = 1 (3 divisions)
# log₂(16) = 4 car 16 ÷ 2 ÷ 2 ÷ 2 ÷ 2 = 1 (4 divisions)
# En recherche dichotomique, c'est le nombre maximum d'étapes nécessaires pour trouver 
# un élément dans un tableau trié de taille N.

print("==== Exercice 5 ====")
# Appliquer l'algorithme dans un contexte différent
print()
# Supposons que vs ayez une liste de noms de personnes, triée par ordre alphabetique.
# Comment pourriez-vs utiliser la recherche dichotomique pour trouver rapidement si un nom specifique est dans la liste ?

# On pourrait utiliser la recherche dichotomique pour trouver rapidement 
# si un nom specifique est dans la liste en utilisant la division par 2 pour trouver l'element. 
# Par exemple: 

# Systèmes de fichiers :
# Recherche rapide dans un index de fichiers triés
# Exemple : Trouver un fichier dans une liste de fichiers triés par date

# Dictionnaires :
# Vérifier si un mot existe dans un dictionnaire
# Exemple : Vérifier l'orthographe d'un mot

