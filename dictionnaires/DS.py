# DS NSI
# Partie 1: Gestion de produits
catalogue = [
("T-shirt", "Vetement", 10.99),
("PC", "Technologie", 19.99),
("Chapeau", "Vetement", 9.99)
]

def ajouter_produit(catalogue, nom, categorie, prix):
    catalogue.append((nom, categorie, prix))

def rechercher_produit(catalogue, nom):
    for produit in catalogue:
        if produit[0] == nom:
            return produit
    return None

# Partie 2: Gestion des clients
# avec ajoutez ici clients sous formes de paires cles valeur (id: (nom,contact))
clients = [
    (1, ("John Doe", "john@gmail.com")),
    (2, ("Jane Smith","jane@gmail.com")),
    (3, ("Bob Johnson","bob.john@gmail.com"))
]

def modifier_client(clients, id, nom, contact):
    clients[id] = (nom, contact)

def afficher_client(clients):
    for client in clients:
        print(client)

# Partie 3: Gestion des Transactions
# ajouter ici quelques transactions sous forme de paire cle valeur
transactions = [
    (1, "2024-01-01", 100.00),
    (2, "2024-01-02", 200.00),
    (3, "2024-01-03", 300.00)
]

def enregistrer_transaction(transactions, id_client, produit, date):
    transactions.append((id_client, produit), date)

def afficher_transactions(transactions):
    for transaction in transactions:
        print(transaction)

# Partie 1 tests:
print("")
print("==============Partie 1 TESTS===============")
print("")
print(catalogue)
print("")
ajouter_produit(catalogue, "Chaise en Bois", "Mobilier", 75)
print(catalogue)
print("")
print(rechercher_produit(catalogue, "Chaise en Bois"))
print("")
print(rechercher_produit(catalogue, "Table en Verre"))
print("")

# Partie 2 TESTS
print("")
print("==============Partie 2 TESTS===============")
print("")
print(clients)
print("")
clients[2] = ("Jean Valjean", "jean@nouveaemail.com")
modifier_client(clients, 2, "Jean Valjean", "jean@nouveaemail.com")
print("")
afficher_client(clients)
print("")
# Partie 3 TESTS
print("==============Partie 3 TESTS===============")
print("")
enregistrer_transaction(transactions, 1, "Chaise en Bois", "2024-01-25")
print(transactions)
print("")
afficher_transactions(transactions)
print("")
