# 2.1 Le problème du rendu de monnaie
def rendu_monnaie(somme_a_rendre, jeu_pieces):
    """ Renvoie la liste des pièces à rendre pour atteindre la somme à rendre.
    - Entrées :
    - somme_a_rendre est un entier : int
    - jeu_pieces contient la liste des pièces disponibles : list(int)
    - Sortie : pieces_rendues est la liste des pièces rendues : list(int)
    """
    jeu_pieces.sort(reverse=True)  # tri décroissant des pièces disponibles
    pieces_rendues = []
    i = 0
    while somme_a_rendre > 0:
        piece = jeu_pieces[i]
        if piece <= somme_a_rendre:
            pieces_rendues.append(piece)
            somme_a_rendre = somme_a_rendre - piece
        else:
            i = i + 1
    return pieces_rendues

# Test
# Test 1 - Cas standard
print()
print("============ Tests: Rendu de monnaie ============")
print()
print("\n=== Test 1: Cas standard ===")
print()
print("Test avec une somme simple (12) et des pièces standards [1, 2, 5, 10]")
print()
print("Attendu: [10, 2] (car 10 + 2 = 12)")
print()
print("Résultat:", rendu_monnaie(12, [1, 2, 5, 10]))
print()

# Test 2 - Somme nulle
print("\n=== Test 2: Somme nulle ===")
print()
print("Test quand il n'y a rien à rendre")
print()
print("Attendu: [] (liste vide)")
print()
print("Résultat:", rendu_monnaie(0, [1, 2, 5, 10]))
print()

# Test 3 - Pièces non standard
print("\n=== Test 3: Pièces non standard ===")
print()
print("Test avec pièces [1, 7, 10] pour 15 (montre la limite de l'algorithme glouton)")
print()
print("Attendu: [7, 7, 1] (solution optimale) ou [10, 1, 1, 1, 1, 1] (solution gloutonne)")
print()
print("Résultat:", rendu_monnaie(15, [1, 7, 10]))
print()
print("Note: L'algorithme glouton ne trouve pas toujours la solution optimale")

# Test 4 - Grand nombre
print("\n=== Test 4: Grand nombre ===")
print()
print("Test avec une grande somme (288) et plusieurs types de pièces")
print()
print("Attendu: [100, 100, 50, 20, 10, 5, 2, 1] (solution optimale)")
print()
print("Résultat:", rendu_monnaie(288, [1, 2, 5, 10, 20, 50, 100]))
print()

# Test 5 - Pièces dans le désordre
print("\n=== Test 5: Pièces dans le désordre ===")
print()
print("Test avec les pièces dans un ordre aléatoire [5, 1, 2]")
print()
print("Attendu: [5, 1] (car l'algorithme trie d'abord les pièces)")
print()
print("Résultat:", rendu_monnaie(6, [5, 1, 2]))
print()



# 2.2 Le problème du sac à dos
def clef_tri(objet):
    """ Renvoie la clef de tri valeur/poids de l'objet.
    - Entrée : objet est un tuple (valeur, poids)
    - Sortie : renvoie un nombre qui est le rapport valeur/poids : float
    """
    (valeur, poids) = objet
    return valeur / poids

def sac_a_dos(objets, poids_maxi):
    """ Renvoie la liste des objets retenus.
    - Entrées :
    - objets est une liste d'objets à choisir
      (chaque objet est une tuple (valeur, poids))
    - poids_maxi est un nombre : float
    - Sortie : la valeur renvoyée est la liste d'objets retenus : list(tuple)
    """
    objets_retenus = []
    objets.sort(key=clef_tri, reverse=True)  # tri de la liste d'objets
    for objet in objets:
        (valeur, poids) = objet
        if poids <= poids_maxi:  # J'ai modifié < en <= pour inclure le cas où le poids est exactement le poids_maxi
            objets_retenus.append(objet)
            poids_maxi = poids_maxi - poids
    return objets_retenus

# Test
print("============ Tests: Sac a dos ============")
print()
# Test 1 - Cas standard
print("\n=== Test 1: Cas standard ===")
print()
print("Test avec des objets standards et un poids maximum de 4")
print()
print("Objets: [(10, 2), (5, 1), (7, 3), (3, 1)]")
print()
print("Poids maximum: 4")
print()
print("Attendu: [(5, 1), (3, 1)] ou [(3, 1), (5, 1)]")
print("(L'algorithme glouton par rapport valeur/poids devrait choisir ces objets)")
print()
print("Résultat:", sac_a_dos([(10, 2), (5, 1), (7, 3), (3, 1)], 4))
print()

# Test 2 - Poids maximum nul
print("\n=== Test 2: Poids maximum nul ===")
print()
print("Test quand le poids maximum est 0")
print()
print("Objets: [(10, 2), (5, 1)]")
print()
print("Poids maximum: 0")
print()
print("Attendu: [] (aucun objet ne peut être pris)")
print()
print("Résultat:", sac_a_dos([(10, 2), (5, 1)], 0))
print()

# Test 3 - Objet trop lourd
print("\n=== Test 3: Objet unique trop lourd ===")
print()
print("Test avec un objet trop lourd pour le sac")
print()
print("Objets: [(10, 5), (3, 1), (2, 1)]")
print()
print("Poids maximum: 3")
print()
print("Attendu: [(3, 1), (2, 1)]")
print("(L'algorithme devrait ignorer l'objet trop lourd (10,5))")
print()
print("Résultat:", sac_a_dos([(10, 5), (3, 1), (2, 1)], 3))
print()

# Test 4 - Limite de l'algorithme glouton
print("\n=== Test 4: Limite de l'algorithme glouton ===")
print()
print("Test montrant que l'algorithme glouton ne trouve pas toujours la solution optimale")
print()
print("Objets: [(60, 10), (100, 20), (120, 30)]")
print()
print("Poids maximum: 50")
print()
print("Solution gloutonne attendue: [(60, 10), (100, 20)]")
print()
print("(Note: La solution optimale serait [(100, 20), (120, 30)] mais l'algorithme glouton ne la trouve pas)")
print()
print("Résultat:", sac_a_dos([(60, 10), (100, 20), (120, 30)], 50))
print()

# Test 5 - Objets avec même ratio
print("\n=== Test 5: Objets avec le même ratio valeur/poids ===")
print()
print("Test avec des objets ayant le même ratio valeur/poids")
print()
print("Objets: [(4, 2), (6, 3), (8, 4)]")
print()
print("Poids maximum: 5")
print()
print("Attendu: [(4, 2), (6, 3)] ou [(6, 3), (4, 2)]")
print()
print("(Tous les objets ont le même ratio valeur/poids = 2)")
print()
print("Résultat:", sac_a_dos([(4, 2), (6, 3), (8, 4)], 5))
print()