# Fusion
# Exemples

# Table "Langue"
print("==========Langue==========")
langues = [
    {"IdLangue": 1, "Langue": "Anglais"},
    {"IdLangue": 2, "Langue": "Français"}
]

for langue in langues:
    print(langue)
print()

# Table "Auteur"
print("==========Auteur==========")
auteurs = [
    {"IdAuteur": 121, "Nom": "Huxley", "Prenom": "Aldous", "IdLangue": 1, "Naissance": 1894},
    {"IdAuteur": 211, "Nom": "Herbert", "Prenom": "Frank", "IdLangue": 1, "Naissance": 1920},
    {"IdAuteur": 305, "Nom": "Orwell", "Prenom": "George", "IdLangue": 1, "Naissance": 1903},
    {"IdAuteur": 306, "Nom": "Asimov", "Prenom": "Isaac", "IdLangue": 2, "Naissance": 1920}
]

for auteur in auteurs:
    print(auteur)
print()

# Table "Livre"
print("==========Livre==========")
livres = [
    {"Titre": "1984", "IdAuteur": 305, "Année": 1949},
    {"Titre": "Dune", "IdAuteur": 211, "Année": 1965},
    {"Titre": "Fondation", "IdAuteur": 306, "Année": 1951},
    {"Titre": "Le meilleur des mondes", "IdAuteur": 121, "Année": 1931}
]

for livre in livres:
    print(livre)
print()

# Défi : trouver les auteurs et les titres des livres publiés en langue anglaise.
print("Défi:trouver les auteurs et les titres des livres publiés en langue anglaise")
# 1. En fusionnant les tables Langue et Auteur en s’appuyant sur leur descripteur commun 
# IdLAngue/Langue, on peut construire la table fusionnée suivante:
langue_auteur = [
    {"IdLAngue": 1, "Langue": "Anglais", "IdAuteur": 121, "Nom": "Huxley", "Prenom": "Aldous", "IdLangue": 1, "Naissance": 1894},
    {"IdLAngue": 1, "Langue": "Anglais", "IdAuteur": 211, "Nom": "Herbert", "Prenom": "Frank", "IdLangue": 1, "Naissance": 1920},
    {"IdLAngue": 1, "Langue": "Anglais", "IdAuteur": 305, "Nom": "Orwell", "Prenom": "George", "IdLangue": 1, "Naissance": 1903},
]
for langue_auteur in langue_auteur:
    print(langue_auteur)
print()

# 2. En fusionnant ensuite cette table avec la table Livre en s’appuyant sur leur descripteur commun
# IdAuteur, on peut construire la table fusionnée suivante :
langue_auteur_livre = [ 
    {"IdAuteur": 121, "Nom": "Huxley", "Prenom": "Aldous", "Naissance": 1894, "Titre": "Le meilleur des mondes", "IdAuteur": 305, "Année": 1931},
    {"IdAuteur": 211, "Nom": "Herbert", "Prenom": "Frank", "Naissance": 1920, "Titre": "Dune", "IdAuteur": 211, "Année": 1965},
    {"IdAuteur": 305, "Nom": "Orwell", "Prenom": "George", "Naissance": 1903, "Titre": "1984", "IdAuteur": 305, "Année": 1949},
]
for langue_auteur_livre in langue_auteur_livre:
    print(langue_auteur_livre)
print()

# 3. On peut finalement ne garder que les champs souhaités (Titres et Auteurs) :
auteur_livre = [
    {"IdAuteur": 121, "Nom": "Huxley", "Prenom": "Aldous", "Titre": "Le meilleur des mondes"},
    {"IdAuteur": 211, "Nom": "Herbert", "Prenom": "Frank", "Titre": "Dune"},
    {"IdAuteur": 305, "Nom": "Orwell", "Prenom": "George", "Titre": "1984"},
]

for auteur_livre in auteur_livre:
    print(auteur_livre)
print()
