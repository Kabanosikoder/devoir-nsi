def utf8_length(s):
    return [len(c.encode('utf-8')) for c in s]

print(utf8_length('guh'))
print(utf8_length('tést'))

