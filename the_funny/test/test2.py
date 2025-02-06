def est_palindrome(texte):
    texte = ''.join(filter(str.isalpha, texte.lower()))
    return texte == texte[::-1]

# Tests
print(est_palindrome("palindrome"))  # False
print(est_palindrome("radar"))  # True
print(est_palindrome("Engage le jeu que je le gagne"))  # True
