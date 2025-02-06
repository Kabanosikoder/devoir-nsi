
def next_year():
    global year  # makes variable global, very useful!!!!
    print("Fin de l'annee", year)
    year += 1
    print("Debut de l'annee", year)

year = 2018
next_year()
next_year()
next_year()