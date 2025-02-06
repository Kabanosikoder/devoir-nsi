def palindrome_checker(word):
    word = word.replace(" ", "").lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return "This is a palindrome"
    else:
        return "This isn't a palindrome"

print(palindrome_checker('kayak'))
print(palindrome_checker('frigo'))

