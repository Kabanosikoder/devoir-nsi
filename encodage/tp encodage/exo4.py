def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        # Vérification si le caractère est une lettre majuscule
        if char.isupper():
            # Décalage pour les lettres majuscules (A-Z)
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Vérification si le caractère est une lettre minuscule
        elif char.islower():
            # Décalage pour les lettres minuscules (a-z)
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Les caractères non alphabétiques ne sont pas modifiés
            encrypted_text += char

    return encrypted_text

texte = "I love Python and Java"
decalage = 3
texte_chiffre = caesar_cipher(texte, decalage)
print(texte_chiffre)

