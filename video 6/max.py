
def max(a, b):
    if a > b:
        return a
    else:
        return b

first_value = int(input("Entrer la valeur de a (la premiere)"))
second_value = int(input("Entrer la valeur de b (la deuxieme)"))
max_value = max(first_value, second_value)
print("La valuer max est:", max_value)