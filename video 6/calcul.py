
def addition(n=45):  # in brackets insert parameters
    result = 5 + n
    return result

def multiply():
    result = 5 * 8
    return result

def get_message():
    return "Le resultat du calcul est"


print(get_message(), addition())  # no parameters thus n = 45 and  result = 50
print(get_message(), addition(4))
print(get_message(), addition(9))
print(get_message(), multiply())