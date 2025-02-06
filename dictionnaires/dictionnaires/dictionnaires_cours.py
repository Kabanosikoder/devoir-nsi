# Dictionnaires cours
print("==== Dictionnaires cours ====")
# 1 Définitions : p-uplet nommés
print("==== 1. Définitions ====")

exif_data = {
"Version Exif" : "Exif version 2.1",
"Date" : "2003:08:11",
"Compression" : "JPEG",
"Espace colorimétrique" : "sRGB",
"Dimension X" : 2240,
"Dimension Y" : 1680
}

print(exif_data["Dimension X"])

exif_data = ("Exif version 2.1", "2003:08:11", "JPEG", "sRGB", 2240, 1680)

print(exif_data[4])
print("")

# 2 Dictionnaires
print("==== 2. Dictionnaires ====")

########## Création d'un dictionnaire #################
print("==== Création d'un dictionnaire ====")
dico = {'Henri':(4,'roi'), 'Louis':(16, 'roi')}
print(dico) # {'Henri': (4, 'roi'), 'Louis': (16, 'roi')} 
print("")

########## Accès à une valeur avec sa clef ############
print("==== Accès à une valeur avec sa clef ====")
print(dico['Henri']) # (4, 'roi')
print("")

########## Ajout d'un élément #########################
print("==== Ajout d'un élément ====")
dico['Élisabeth'] = (1,'reine')
print(dico) # {'Henri': (4, 'roi'), 'Louis': (16, 'roi'), 'Élisabeth': (1, 'reine')}
print("")

########## Modification d'un élément ##################
print("==== Modification d'un élément ====")
dico['Élisabeth'] = (2,'reine')
print(dico) # {'Henri': (4, 'roi'), 'Louis': (16, 'roi'), 'Élisabeth': (2, 'reine')}
print("")

# 3 Itérations sur les dictionnaires
print("==== 3. Itérations sur les dictionnaires ====")

# Pour itérer sur les items complets (couples clef/valeur) :
for (clef, valeur) in dico.items():
    print(f"La valeur {valeur} est associée à la clef {clef}")
print("")

# La valeur (4, 'roi') est associée à la clef Henri
# La valeur (16, 'roi') est associée à la clef Louis
# La valeur (2, 'reine') est associée à la clef Élisabeth

# Pour itérer sur les clefs :
for clef in dico.keys():
    print(clef)
print("")
# Henri
# Louis
# Élisabeth

# Pour itérer sur les valeurs :
for valeur in dico.values():
    print(valeur)
print("")
# (4, 'roi')
# (16, 'roi')
# (2, 'reine')