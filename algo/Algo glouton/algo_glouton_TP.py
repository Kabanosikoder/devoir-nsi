# TP: Algo Gloutons
# Problème 1: Rendu de monnaie
 # Exercice 1:
 # 1. Ecrire une fonction en python qui prend en entrée une somm a rendre et une list de valuers de pieces, et qui renvoie une liste
 # de pièces a rendre pour atteindre la somme a rendre.

def rendu_monnaie(somme_a_rendre, jeu_pieces):
    jeu_pieces.sort(reverse=True)
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

print("Liste de pièces rendues:")
print(rendu_monnaie(12, [1, 2, 5, 10]))

# 2. Testez votre fonction avec différentes valeurs de somme a rendre et de pieces disponibles.

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

# 3. Quelle est la complexité de votre algorithme ?
# La complexité est O(nlogn) car on trie la liste des pièces.


# Problème 2: Sac à dos
# Exercice 2:
# 1. Ecrire une fonction en python qui prend en entrée une liste d'objets et le poids maximal que peut supporter le sac a dos et qui renvoie une liste 
# des objets a mettre dans le sac a dos pour maximiser la valeur totale.

def clef_tri(objet):
    (valeur, poids) = objet
    return valeur / poids

def sac_a_dos(objets, poids_maxi):
    objets_retenus = []
    objets.sort(key=clef_tri, reverse=True)
    for objet in objets:
        (valeur, poids) = objet
        if poids <= poids_maxi:
            objets_retenus.append(objet)
            poids_maxi = poids_maxi - poids
    return objets_retenus

print("Liste des objets retenus:")
print(sac_a_dos([(10, 2), (5, 1), (7, 3), (3, 1)], 4))
print()

# 2. Testez votre fonction avec différentes valeurs de poids maximal et de liste d'objets.

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

# 3. Quelle est la complexité de votre algorithme ?
# La complexité est O(nlogn).



# Problème 3: Repartition de taches
# Exercice 3:
# 1. Ecrire une fonction en python qui prend en entrée le nombre de libres,le nombre de chercheurs et une liste du nombres de pages de chaque livre
# et qui renvoie le nombre maximum de pages que doit lire un chercheur.

def repartition_taches(nbr_libres, nbr_chercheurs, pages):
    if not pages or nbr_chercheurs <= 0:
        return []
    pages.sort(reverse=True)
    pages_reparties = []
    i = 0
    while i < nbr_chercheurs and i < len(pages):
        pages_reparties.append(pages[i])
        i += 1
    return pages_reparties

print("Liste des pages reparties:")
print(repartition_taches(2, 3, [10, 20, 30, 40, 50]))
print()

# 2. Testez votre fonction avec différentes valeurs:
print("============ Tests: Repartition de taches ============")
print()
print("=== Test 1: Cas standard ===")
print()
print("Test avec 2 libres, 3 chercheurs et des pages [10, 20, 30, 40, 50]")
print()
print("Attendu: [10, 20, 30]")
print()
print("Résultat:", repartition_taches(2, 3, [10, 20, 30, 40, 50]))
print()

# Test 2 - Nombre de chercheurs nul
print("\n=== Test 2: Nombre de chercheurs nul ===")
print()
print("Test quand le nombre de chercheurs est 0")
print()
print("Attendu: [] (aucun chercheur)")
print()
print("Résultat:", repartition_taches(2, 0, [10, 20, 30, 40, 50]))
print()

# Test 3 - Nombre de libres nul
print("\n=== Test 3: Nombre de libres nul ===")
print()
print("Test quand le nombre de libres est 0")
print()
print("Attendu: [] (aucun livre)")
print()
print("Résultat:", repartition_taches(0, 3, [10, 20, 30, 40, 50]))
print()

# Test 4 - Nombre de pages nul
print("\n=== Test 4: Nombre de pages nul ===")
print()
print("Test quand le nombre de pages est 0")
print()
print("Attendu: [] (aucune page)")
print()
print("Résultat:", repartition_taches(2, 3, []))
print()

# Test 5 - Nombre de pages nul
print("\n=== Test 5: Nombre de pages nul ===")
print()
print("Test quand le nombre de pages est 0")
print()
print("Attendu: [] (aucune page)")
print()
print("Résultat:", repartition_taches(2, 3, []))
print()

# Quelle est la complexité de l'algorithme ?
# La complexité est O(nlogn).