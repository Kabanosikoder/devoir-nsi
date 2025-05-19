# Selection:
def tri_selection(tab):
    """ Trie le tableau par sélection avec affichage de l'invariant """
    print("\n====Tri par sélection====")
    print(f"Tableau initial : {tab}")
    
    for i in range(len(tab) - 1):
        indice_min = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
        
        # Afficher l'état et l'invariant
        print(f"\nItération {i+1} : {tab}")
        print(f"Invariant : Les {i+1} premiers éléments {tab[:i+1]} sont triés et sont les {i+1} plus petits éléments.")
    
    return tab

def tri_insertion(tab):
    """ Trie le tableau par insertion avec affichage de l'invariant """
    print("\n====Tri par insertion====")
    print(f"Tableau initial : {tab}")
    
    for i in range(1, len(tab)):
        element = tab[i]
        j = i - 1
        
        while j >= 0 and element < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        
        tab[j + 1] = element
        
        # Afficher l'état et l'invariant
        print(f"\nItération {i} : {tab}")
        print(f"Invariant : Les {i+1} premiers éléments {tab[:i+1]} forment un sous-tableau trié.")
    
    return tab

# Tableau à trier
tableau = [8, 3, 5, 1]

# Trier avec les deux méthodes
tri_selection(tableau.copy())
# On utilise .copy() pour ne pas modifier le tableau original
tri_insertion(tableau.copy())
print()

# Bonus : Proposer un autre invariant pour l’un des deux tris.

def tri_insertion_avec_invariant_alternatif(tab):
    print("\n====Tri par insertion (invariant bonus)====")
    print(f"Tableau initial : {tab}")
    
    for i in range(1, len(tab)):
        element = tab[i]
        j = i - 1
        
        while j >= 0 and element < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        
        tab[j + 1] = element
        
        # Afficher l'état et l'invariant alternatif
        print(f"\nItération {i} : {tab}")
        print(f"Invariant alternatif : Les {i+1} premiers éléments {tab[:i+1]} sont une permutation triée du début du tableau original.")
    
    return tab

# Exemple d'utilisation
tableau = [8, 3, 5, 1]
tri_insertion_avec_invariant_alternatif(tableau.copy())
print()