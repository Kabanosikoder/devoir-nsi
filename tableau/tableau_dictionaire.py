# Les Tableau et Dictionnaire en Python
# Excercice 1: Creation d'un tableau sans utiliser de bibliotheque
print("===== Exercice 1 =====")

print("Tableau basic avec python 3 -sans numpy-")

t = [[1,2,3,4,5] ,
    [6,7,8,9,0]  ,
    [0,0,0,0,0]  ]

# Methode 1
print("===== Methode 1 =====")
for y in range(3):
    for x in range(5):
        print(t[y][x], end=' ')
    print()

# Methode 2
print("===== Methode 2 =====")
for y in range(3):
    print(' '.join(str(t[y][x]) for x in range(5)))

# Methode 3
print("===== Methode 3 =====")
y = 0
while y < 3:
    x = 0
    while x < 5:
        print(t[y][x], end=' ')
        x += 1
    print()
    y += 1