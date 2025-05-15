def recherche_dichotomique(tab, val):
    """
    Effectue une recherche dichotomique de la valeur dans le tableau trié.
    
    Args:
        tab (list): Tableau trié d'éléments comparables
        val: Valeur à rechercher dans le tableau
        
    Returns:
        int: L'index de la valeur si trouvée, -1 sinon
    """
    igauche = 0  # borne de recherche inférieure
    idroite = len(tab) - 1  # borne de recherche supérieure
    
    while igauche <= idroite:
        imilieu = (igauche + idroite) // 2
        
        if tab[imilieu] == val:  # val trouvée dans le tableau
            return imilieu
        elif tab[imilieu] > val:  # chercher dans la moitié gauche
            idroite = imilieu - 1
        else:  # chercher dans la moitié droite
            igauche = imilieu + 1
            
    return -1  # valeur non trouvée

# Expliquer l'algo et faire des tests

print(recherche_dichotomique([1, 2, 3, 4, 5], 3)) # devrait retourner 2
print(recherche_dichotomique([1, 2, 3, 4, 5], 6)) # devrait retourner -1
print(recherche_dichotomique([1, 2, 3, 4, 5], 1)) # devrait retourner 0
print(recherche_dichotomique([1, 2, 3, 4, 5], 5)) # devrait retourner 4
print(recherche_dichotomique([1, 2, 3, 4, 5], 0)) # devrait retourner -1
print(recherche_dichotomique([1, 2, 3, 4, 5], 2)) # devrait retourner 1
print(recherche_dichotomique([1, 2, 3, 4, 5], 4)) # devrait retourner 3

# Expliquation de l'algo
# L'algo de dichotiomie est un algo de recherche qui permet de trouver un element dans un tableau trié