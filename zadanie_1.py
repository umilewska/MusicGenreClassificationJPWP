# ZADANIE 1
# Uzupełnij poniższe funkcje tak, aby wskazały najbliższego sąsiada.
# Do porównania wyników podano fragment kodu, gdzie do znalezienia najbliższego sąsiada
# została użyta biblioteka sklearn.

import numpy as np
from sklearn.neighbors import NearestNeighbors

x_train = np.random.rand(10, 3)
x_test = np.random.rand(3)

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        # miejsce na twój kod
        pass
    return 0

def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf

    # miejsce na twój kod


    print("twoja funkcja:")
    print(nearest)

nearest(x_train, x_test)
neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(x_train)
print("\nsklearn.neighbors:")
print(neigh.kneighbors([x_test], 1)[1][0][0])
