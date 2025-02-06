def est_pangramme(chaine):
    chaine = chaine.lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    lettres_dans_chaine = set(chaine)
    return alphabet.issubset(lettres_dans_chaine)

# Tests
print(est_pangramme("pangramme")) # False
print(est_pangramme("Portez ce vieux whisky au juge blond qui fume"))  # True
print(est_pangramme("the quick brown fox jumps over the lazy dog"))  # True
print(est_pangramme("Dans un wagon bleu, tout en mangeant cinq kiwis frais, vous jouez du xylophone"))  # True
