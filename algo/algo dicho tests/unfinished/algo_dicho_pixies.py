def recherche_dichotomique(t, x):
    tr = False
    deb = 0 
    fin = len(t) - 1
    
    while not tr and deb <= fin:
        mil = (deb + fin) // 2
        if t[mil] == x:
            tr = True
        else:
            if x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1
                
    return tr

# À faire vous-même 1

def recherche_dichotomique(t, x):
    # Initialisation
    tr = False  # Variable pour suivre si on a trouvé l'élément
    deb = 0      # Indice de début du sous-tableau courant
    fin = len(t) - 1  # Indice de fin du sous-tableau courant
    
    # Tant qu'on n'a pas trouvé l'élément et qu'il reste des éléments à examiner
    while not tr and deb <= fin:
        # 1. Calcul du milieu du sous-tableau courant
        mil = (deb + fin) // 2
        
        # 2. Si on trouve l'élément au milieu
        if t[mil] == x:
            tr = True  # On a trouvé l'élément
        else:
            # 3. Si l'élément recherché est dans la moitié droite
            if x > t[mil]:
                deb = mil + 1  # On élimine la moitié gauche
            # 4. Si l'élément recherché est dans la moitié gauche
            else:
                fin = mil - 1  # On élimine la moitié droite
                
    # On renvoie Vrai si trouvé, Faux sinon
    return tr

# Exemple d'utilisation
if __name__ == "__main__":
    tableau = [5, 7, 12, 14, 23, 27, 35, 40, 41, 45]
    print(recherche_dichotomique(tableau, 35))  # True
    print(recherche_dichotomique(tableau, 42))  # False