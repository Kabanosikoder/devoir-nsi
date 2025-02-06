# Niveau Débutant
print("")
print("Niveau Débutant")
# ====Exercice 1====
print("====Exercice 1====")
# Créez un dictionnaire pour stocker les informations d'un livre : titre, auteur,
# année de publication et éditeur.

book = {
    "title": "Titre du livre",
    "author": "Auteur du livre",
    "publication_year": 1999,
    "publisher": "Éditeur du livre"
}
print(book)
print("")

# ====Exercice 2====
# Pour le dictionnaire créé précédemment, accédez à l'information "année de publication"

print("====Exercice 2====")
publication_year = book["publication_year"]
print("Année de publication:", publication_year)
print("")

# Niveau Intermédiaire
print("Niveau Intermédiaire")

# ====Exercice 3====
# Ajoutez au dictionnaire du livre une nouvelle paire clé-valeur qui indique le genre du livre.

print("====Exercice 3====")
book["genre"] = "Genre du livre"
print("Genre du livre:", book["genre"])
print("")

# Niveau Avancé
print("Niveau Avancé")

# ====Exercice 4====
# Modifiez la valeur de la clé "éditeur" dans le dictionnaire du livre

print("====Exercice 4====")
book["publisher"] = "Nouvel éditeur"
print("Éditeur du livre:", book["publisher"])
print("")

# ====Exercice 5====
# Utilisez une boucle pour afficher toutes les clés du dictionnaire du livre.

print("====Exercice 5====")
print("Clés du dictionnaire:")
for key in book.keys():
    print(key)
print("")

# ====Exercice 6====
# Utilisez une boucle pour afficher toutes les valeurs du dictionnaire du livre

print("====Exercice 6====") 
print("Valeurs du dictionnaire:")
for value in book.values():
    print(value)
print("")

# ====Exercice 7====
print("====Exercice 7====")
# Utilisez une boucle pour afficher toutes les clés et leurs valeurs correspondantes du dictionnaire du livre.

print("Clés et valeurs du dictionnaire:")
for key, value in book.items():
    print(f"{key}: {value}")
print("")