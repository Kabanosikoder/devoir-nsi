# PARTIE PRATIQUE:
# Système de Gestion de Bibliothèque en Python

# Contexte:
# Vous êtes en charge de développer un système de gestion pour une bibliothèque. Ce
# système doit gérer les livres, les adhérents et les prêts en utilisant Python.



# Partie 1 : Gestion des Livres
# 1. Création du Catalogue de Livres
# Initialisez le catalogue de livres.

catalogue = [
    ("Le Petit Prince", "Antoine de Saint-Exupéry", 1943),
    ("1984", "George Orwell", 1949),
    ("To Kill a Mockingbird", "Harper Lee", 1960)
]


# 2. Fonction pour Ajouter un Livre
# Complétez la fonction pour ajouter un livre au catalogue.
def ajouter_livre(catalogue, titre, auteur, annee):
    catalogue.append((titre, auteur, annee))

 # C) catalogue.append((titre, auteur, annee))


# 3. Fonction pour Rechercher un Livre
# Complétez la fonction pour rechercher un livre par son titre.
def rechercher_livre(catalogue, titre):
 for livre in catalogue:
  if livre[0] == titre:
   return livre



 # Partie 2 : Gestion des Adhérents
# 1. Enregistrement des Adhérents
# Initialisez le dictionnaire des adhérents.

adherents = {
    1: ("John", 30),
    2: ("Bob", 25),
    3: ("Charles", 35)
}


# 2. Fonction pour Modifier un Adhérent
# Complétez la fonction pour modifier les informations d'un adhérent.
def modifier_adherent(adherents, numero, nom, age):
    adherents[numero] = (nom, age)


# 3. Fonction pour Afficher les Adhérents
# Complétez la fonction pour afficher tous les adhérents.
def afficher_adherents(adherents):
 for adherent in adherents:
  print(adherent)
 print("")



# Partie 3 : Gestion des Prêts
# 1. Enregistrement des Prêts
# Initialisez le dictionnaire des prêts.

prets = {
 1: ("Le Petit Prince", 1, "2026-01-01"),
 2: ("1984", 2, "2034-02-01"),
 3: ("To Kill a Mockingbird", 3, "2090-03-01")
}


#2. Fonction pour Enregistrer un Retour de Livre
# Complétez la fonction pour gérer le retour d'un livre.
print("")
def retour_livre(prets, numero_adherent, titre_livre):
    if (numero_adherent, titre_livre) in prets:
        del prets[numero_adherent, titre_livre]
    print("Le livre a bien été retourné.")


# 3. Fonction pour Abicher les Prêts en Cours
# Complétez la fonction pour abicher la liste des prêts en cours.
def afficher_prets(prets):
 for pret in prets:
  print(pret)
 print("")



# TEST
print("==============TEST==============")
print("")
print("====Partie 1 : Gestion des Livres====")
print("")

ajouter_livre(catalogue, "Le Comte de Monte-Cristo", "Alexandre Dumas", 1943)
print("Nouveau catalogue:")
print(catalogue)
print("")

rechercher_livre(catalogue, "Le Comte de Monte-Cristo")
print("Informations sur le livre 'Le Comte de Monte-Cristo':")
print("")

print(rechercher_livre(catalogue, "1984"))
print("")



print("====Partie 2 : Gestion des Adhérents====")
print("")

# Tester l'Enregistrement d'un Nouvel Adhérent
adherents[3] = ("Jean Valjean", 40)
afficher_adherents(adherents)

# Tester la Modification des Informations d'un Adhérent
modifier_adherent(adherents, 1, "Alice Dupont", 26)
afficher_adherents(adherents)

print("====Partie 3 : Gestion des Prêts====")
print("")

# Tester l'Enregistrement d'un Nouveau Prêt
prets[(1, "Le Petit Prince")] = "2024-03-01"
print(prets)

# Tester le Retour d'un Livre
retour_livre(prets, 2, "1984")
afficher_prets(prets)