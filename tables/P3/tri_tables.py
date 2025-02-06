# Tri de la table
# Exemples

# 3.1 Tri d’une liste simple
print("==========3.1==========")
liste = [8, 10, 1, 3]
print("Original List:")
print(liste)
print("Sorted List:")
print(sorted(liste, reverse=True))
print()

liste = ["trèfle", "carreau", "coeur", "pique"]
print("Original List:")
print(liste)
print("Sorted List:")
print(sorted(liste))
print()

# 3.2 Tri d’une liste de tuples
print("==========3.2==========")
liste = [(8, 'trèfle'), (10, 'carreau'), (1, 'coeur'), (3, 'pique')]
print("Original List:")
print(liste)
print("Sorted List:")
print(sorted(liste))
print()

def clef(t):
# Fonction de clef de tri.
# Ici on indique qu'on désire trier sur le 2ème élément d'un tuple
    return t[1]
print(sorted(liste, key=clef))
print()

sorted(liste, key=lambda t:t[1])
print()

# 3.3 Tri d’une liste de dictionnaires
print("==========3.3==========")
liste = [{'nom': '8 de trèfle', 'hauteur': 8, 'couleur': 'trèfle'},
{'nom': '10 de carreau', 'hauteur': 10, 'couleur': 'carreau'},
{'nom': 'As de coeur', 'hauteur': 1, 'couleur': 'coeur'},
{'nom': '3 de pique', 'hauteur': 3, 'couleur': 'pique'}]

print(sorted(liste, key=lambda d:d['hauteur']))
print()

print(sorted(liste, key=lambda d:len(d['nom']), reverse=True))
print()