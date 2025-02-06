import csv
from collections import defaultdict

class PrenomManager:
    def __init__(self):
        self.prenoms_combines = []

    def importer_donnees(self, fichier_combines):
        with open(fichier_combines, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            self.prenoms_combines = list(reader)

    def exporter_donnees(self, nom_fichier):
        with open(nom_fichier, mode='w', newline='', encoding='utf-8-sig') as sortie:
            fieldnames = self.prenoms_combines[0].keys()  # Utiliser les clés du premier dictionnaire comme en-tête
            writer = csv.DictWriter(sortie, fieldnames=fieldnames)
            writer.writeheader()  # Écrire l'en-tête
            writer.writerows(self.prenoms_combines)  # Écrire les lignes combinées

    def afficher_prenoms(self):
        self.prenoms_combines.sort(key=lambda x: int(x['nombre']), reverse=True)
        for index, prenom in enumerate(self.prenoms_combines[:10]):  # Afficher les 10 premiers prénoms
            print(f"Prénom n°{index + 1} = {prenom['prenom']} - Occurrence = {prenom['nombre']}")

    def afficher_prenoms_filles_garcons(self):
        jointure = defaultdict(int)
        for prenom in self.prenoms_combines:
            jointure[prenom['prenom']] += int(prenom['nombre'])

        prenoms_filles = {k: v for k, v in jointure.items() if k in ['MANON', 'LEA']}  # Exemple de prénoms de filles
        prenoms_garcons = {k: v for k, v in jointure.items() if k in ['LUCAS', 'THEO']}  # Exemple de prénoms de garçons

        for index, (prenom, occurrence) in enumerate(sorted(prenoms_filles.items(), key=lambda x: x[1], reverse=True)[:10]):
            print(f"Prénom Fille n°{index + 1} = {prenom} - Occurrence = {occurrence}")

        for index, (prenom, occurrence) in enumerate(sorted(prenoms_garcons.items(), key=lambda x: x[1], reverse=True)[:10]):
            print(f"Prénom Garçon n°{index + 1} = {prenom} - Occurrence = {occurrence}")

# Utilisation de la classe
if __name__ == "__main__":
    manager = PrenomManager()
    manager.importer_donnees('Prenoms2003-2004.csv')
    manager.exporter_donnees('Prenoms2003-2004.csv')  # Si vous souhaitez réécrire le même fichier
    manager.afficher_prenoms()
    manager.afficher_prenoms_filles_garcons()