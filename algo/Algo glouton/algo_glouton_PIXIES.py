# TP Pixies
# https://pixees.fr/informatiquelycee/n_site/nsi_prem_glouton_algo.html

# À faire vous-même 1

def sac_a_dos(objets, poids_max):
    objets_tries = sorted(objets, 
                         key=lambda x: x[0]/x[1], 
                         reverse=True)
    
    valeur_totale = 0
    masse_totale = 0
    objets_choisis = []
    
    for valeur, masse in objets_tries:
        if masse_totale + masse <= poids_max:
            objets_choisis.append((valeur, masse))
            valeur_totale += valeur
            masse_totale += masse
    
    return valeur_totale, masse_totale, objets_choisis

def rendu_monnaie(montant, pieces_disponibles):
    pieces_disponibles.sort(reverse=True)
    rendu = {}
    
    for piece in pieces_disponibles:
        if montant >= piece:
            nb_pieces = montant // piece
            rendu[piece] = nb_pieces
            montant -= nb_pieces * piece
            if montant == 0:
                break
                
    return rendu

# Test du sac à dos avec l'exemple du cours
objets = [
    (700, 13),  # (valeur, masse)
    (400, 12),
    (300, 8),
    (300, 10)
]
poids_max = 30

valeur, masse, selection = sac_a_dos(objets, poids_max)
print("=== Problème du sac à dos ===")
print(f"Objets disponibles: {objets}")
print(f"Poids maximum: {poids_max} kg")
print(f"Solution gloutonne: {selection}")
print(f"Valeur totale: {valeur} €")
print(f"Masse totale: {masse} kg")
print("(La solution optimale serait [(700, 13), (400, 12)] avec 1100 € et 25 kg)")

# À faire vous-même 2

pieces = [1, 2, 5, 10, 20, 50, 100, 200]  # en centimes
montant = 347  # 3,47 €

print("\n=== Problème du rendu de monnaie ===")
print(f"Montant à rendre: {montant//100}€{montant%100:02d}")
print("Pièces disponibles (en centimes):", sorted(pieces, reverse=True))
resultat = rendu_monnaie(montant, pieces)

print("Rendu optimal:")
for piece, nb in sorted(resultat.items(), reverse=True):
    if piece >= 100:
        print(f"  - {nb} pièce(s) de {piece//100}€")
    else:
        print(f"  - {nb} pièce(s) de {piece}c")

def test_rendu_2_63():
    """Exercice 2: Application manuelle de la méthode gloutonne pour 2,63€"""
    montant = 263  # 2,63 € en centimes
    pieces = [200, 100, 50, 20, 10, 5, 2, 1]  # en centimes, triées par ordre décroissant
    
    print("\n=== Exercice 2: Rendu de 2,63€ ===")
    print("Méthode gloutonne:")
    
    reste = montant
    pieces_utilisees = []
    
    for piece in pieces:
        if reste >= piece:
            nb = reste // piece
            pieces_utilisees.append((piece, nb))
            reste -= nb * piece
            print(f"  - {nb} pièce(s) de {piece//100}€{piece%100:02d}")
            if reste == 0:
                break
    
    total_pieces = sum(nb for (piece, nb) in pieces_utilisees)
    print(f"\nTotal: {total_pieces} pièces")
    return pieces_utilisees

def rendu_monnaie_avec_details(montant, pieces_disponibles):
    pieces_disponibles = sorted(pieces_disponibles, reverse=True)
    rendu = {}
    total_pieces = 0
    
    print(f"\nRendu de {montant//100}€{montant%100:02d}:")
    
    for piece in pieces_disponibles:
        if montant >= piece:
            nb_pieces = montant // piece
            rendu[piece] = nb_pieces
            total_pieces += nb_pieces
            montant -= nb_pieces * piece
            if piece >= 100:
                print(f"  - {nb_pieces} pièce(s) de {piece//100}€")
            else:
                print(f"  - {nb_pieces} pièce(s) de {piece}c")
            if montant == 0:
                break
                
    print(f"Total: {total_pieces} pièces")
    return total_pieces

# À faire vous-même 3

# Test de l'exercice 2
test_rendu_2_63()

# Test de l'exercice 3
print("\n=== Exercice 3: Algorithme de rendu de monnaie ===")
montant_test = 263  # 2,63 €
pieces_dispo = [200, 100, 50, 20, 10, 5, 2, 1]
total = rendu_monnaie_avec_details(montant_test, pieces_dispo)
print()