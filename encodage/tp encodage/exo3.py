def count_vowels_consonants(s):
    s = s.lower()  # Convert the string to lowercase
    count_vowels = sum(1 for c in s if c in 'aeiou')  # Count vowels
    count_consonants = sum(1 for c in s if c.isalpha() and c not in 'aeiou')  # Count consonants
    return count_vowels, count_consonants

print(count_vowels_consonants('goober goober pumpkin eater'))

