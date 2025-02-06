def cesar(texte, n):
    texte = ''.join(filter(str.isalpha, texte.upper()))
    resultat = ''

    for char in texte:
        nouvelle_lettre = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
        resultat += nouvelle_lettre

    return resultat

# Tests
print(cesar("Quand tout est permis, rien n'est possible", 3))  # TXDQGWRXWHVWSHUPLVRIHQQHVWSRVVLEOH
print(cesar("Quand tout est permis, rien n'est possible", 7))  # XBHUKAVBALZAWLYTPZYPLUULZAWVZZPISL
print(cesar("Quand tout est permis, rien n'est possible", 26))  # QUANDTOUTESTPERMISRIENNESTPOSSIBLE
