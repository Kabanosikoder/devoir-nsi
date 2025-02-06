def ascii_converter(word):

  for character in word:
    ascii = ord(character)
    print(f"Le caractère '{character}' a pour code ASCII : {ascii}")

word = "Testing testing 123"
ascii_converter(word)

