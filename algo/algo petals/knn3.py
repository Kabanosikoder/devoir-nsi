import pandas
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Traitement CSV
iris = pandas.read_csv("iris.csv")
x = iris.loc[:, "petal_length"]
y = iris.loc[:, "petal_width"]
lab = iris.loc[:, "species"]
# Fin traitement CSV

# Valeurs
longueur = 2.5
largeur = 0.75
k = 5  # Modification de k à 5
# Fin valeurs

# Graphique
plt.axis('equal')
plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
plt.scatter(x[lab == 1], y[lab == 1], color='r', label='versicolor')
plt.scatter(x[lab == 2], y[lab == 2], color='b', label='virginica')
plt.scatter(longueur, largeur, color='k')
plt.legend()
# Fin graphique

# Algo knn
d = list(zip(x, y))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(d, lab)

# Prédiction
point = [(longueur, largeur)]
prediction = model.predict(point)
print(f"Pour k={k}, la fleur est prédite comme étant de la classe {prediction[0]}")

plt.show()