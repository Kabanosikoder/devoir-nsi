# Exercice 1: Créez un dictionnaire qui stocke les informations suivantes sur une personne :
# nom, âge, ville de résidence.
print("====Exercice 1====")

person = {
    "name": "Nom de la personne",
    "age": 30,
    "city": "Ville de résidence"
}
print(person)
print("")

# Exercice 2
# Accédez à l'âge de la personne dans le dictionnaire créé dans l'exercice précédent.
print("====Exercice 2====")
age = person["age"]
personne = {
    "nom": "Jean-Baptiste",
    "âge": 35,
    "ville": "Aix-en-Provence"
}
print(personne["âge"])
print("")

# Exercice 3
print("====Exercice 3====")
# : Complétez le code Python suivant pour ajouter un nouveau champ "profession" à votre dictionnaire.
personne = {
    "nom": "Durand",
    "âge": 35,
    "ville": "Paris"
}
# Ajoutez ici le code pour ajouter la profession à votre dictionnaire
personne["profession"] = "Ingénieur"
print(personne)
print("")

# Exercice 4
print("====Exercice 4====")
# Transformez l'algorithme suivant en fonction Python:
#• Algorithme : Pour chaque paire clé-valeur dans un dictionnaire, imprimez la clé et la valeur.

def print_key_value_pairs(dictionnaire):
    for key, value in dictionnaire.items():
        print(f"{key}: {value}")

print_key_value_pairs(personne)
print("")

# Exercice 5
print("====Exercice 5====")
# Transformez l'algorithme suivant en fonction Python:
#• Algorithme : Pour un dictionnaire donné et une clé donnée, renvoie la valeur associée à cette clé.

def get_value_by_key(dictionnaire, key):
    return dictionnaire.get(key, "Clé non trouvée")

print(get_value_by_key(personne, "profession"))
print("")