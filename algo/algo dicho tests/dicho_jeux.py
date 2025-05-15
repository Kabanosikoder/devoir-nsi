def jeu_devine_nombre():
    print("Pensez à un nombre entre 1 et 100. Je vais essayer de le deviner !")
    print("Répondez par 'plus' si le nombre est plus grand, 'moins' s'il est plus petit, ou 'oui' si j'ai trouvé !")
    
    min_nombre = 1
    max_nombre = 100
    tentative = 0
    
    while True:
        proposition = (min_nombre + max_nombre) // 2
        tentative += 1

        reponse = input(f"Est-ce {proposition} ? ").lower().strip()
        
        if reponse == 'oui':
            print(f"Super ! J'ai trouvé en {tentative} tentatives !")
            break
        elif reponse == 'plus':
            min_nombre = proposition + 1
        elif reponse == 'moins':
            max_nombre = proposition - 1
        else:
            print("Veuillez répondre par 'plus', 'moins' ou 'oui'.")
            tentative -= 1
            continue
        
        if min_nombre > max_nombre:
            print("Je pense que vous avez triché !")
            break

if __name__ == "__main__":
    print("=== Jeu du nombre mystère ===")
    while True:
        jeu_devine_nombre()
        rejouer = input("Voulez-vous rejouer ? (oui/non): ").lower().strip()
        if rejouer != 'oui':
            print("Merci d'avoir joué ! Au revoir !")
            break
