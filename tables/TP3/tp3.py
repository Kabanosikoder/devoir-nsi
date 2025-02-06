# TP Python : Traitement de donn´ees en table - Tri de tables
# 2 Tri avec sort et sorted
# 2.2 Exercice
print("=======2.2======")

l = [4, 5, 7, 2, -1, 9]
l_triee = sorted(l)
print("Liste originale :", l)
print("Liste triée :", l_triee)
l.sort()
print("Liste triée en place :", l)
print()
# Expliquez la différence entre sort() et sorted().
# sorted() renvoie une nouvelle liste triée, tandis que sort() modifie la liste originale

# 3 Tri avec le paramètre reverse
# 3.2 Exercice
print("=======3.2======")

l = [4, 5, 7, 2, -1, 9]
l.sort(reverse=True)
print(l)
print()

# 2. Expliquez l’effet du paramètre reverse.
# Le parametre reverse=True indique a sort() de trier la liste dans l’ordre croissant, tandis que reverse=False indique un tri dans l’ordre decroissant.

# 4 Tri selon une clé spécifique
# 4.2 Exercice
print("=======4.2======")
carnet = [
    (" Martin ", " Franck ", 12, " Caen "),
    (" Henri ", " Philippe ", 42, " Nice "),
    (" Lavoisier ", " Antoine ", 12, " Tours "),
    (" Martin ", " Antoine ", 17, " Caen "),
    (" Lovelace ", " Ada ", 36, " Londres ")
]

carnet_age = sorted(carnet, key=lambda personne: personne[2])
for personne in carnet_age:
    print(personne)
print()

# 2. Expliquez l’utilisation du paramètre key.
# key est une fonction qui prend en parametre chaque personne du carnet et qui retourne l’element de cette personne sur lequel il faut trier.
# 3. Modifiez le code pour trier par ville.
print("Trier par ville")
carnet = [
    (" Martin ", " Franck ", 12, " Caen "),
    (" Henri ", " Philippe ", 42, " Nice "),
    (" Lavoisier ", " Antoine ", 12, " Tours "),
    (" Martin ", " Antoine ", 17, " Caen "),
    (" Lovelace ", " Ada ", 36, " Londres ")
]

carnet_ville = sorted(carnet, key=lambda personne: personne[3])
for personne in carnet_ville:
    print(personne)
print()

# 5 Exercices avancés
# 1. Trier le carnet de contacts ci-dessus par longueur du nom de famille.
carnet = [
    ("Martin", "Franck", 12, "Caen"),
    ("Henri", "Philippe", 42, "Nice"),
    ("Lavoisier ", "Antoine", 12, "Tours"),
    ("Martin", "Antoine", 17, "Caen"),
    ("Lovelace", "Ada", 36, "Londres")
]
print("Trier par longueur du nom de famille")
carnet_nom = sorted(carnet, key=lambda personne: len(personne[0]))
for personne in carnet_nom:
    print(personne)
print()
# 2. Trier une liste de mots selon leur longueur en ordre décroissant
mots = [" ordinateur ", " table ", " voiture ", " python ", " exemple "]

mots_long = sorted(mots, key=lambda mot: len(mot), reverse=True)
for mot in mots_long:
    print(mot)
print()
# 3. Justifiez les résultats obtenus.
# Les mots sont triés en ordre décroissant selon leur longueur.