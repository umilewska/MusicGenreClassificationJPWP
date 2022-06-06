#ZADANIE 3 - zrozumienie znaczenia miary odległości
'''poniżej przedstawiona została sytuacja rozmieszczenia na planszy pewnych punktów.
Dla wizualizacji po uruchomieniu programu zobaczysz plansze.
Twoim zadaniem będzie napisanie funkcji obliczającej odległość nieznanego obiektu do
każdego punktu ze znanych grup według miary Euklidesowej i Manhattan.
Zwróć uwagę do jakich grup został przypisany nowy obiekt w zależności od zastosowanej miary.'''

import matplotlib.pyplot as plt
from math import sqrt
import operator

A = [10, 7], [1, 6],
B = [3, 5, 9], [1, 4, 4],
N = [8], [2]

plt.scatter(A[0], A[1], label='Grupa A')
plt.scatter(B[0], B[1], label='Grupa B')
plt.scatter(N[0], N[1], label='Grupa Nieznana')

plt.xlabel('X - Szerokość')
plt.ylabel('Y - Wysokość')
plt.legend()
plt.show()

#Miara Euklidesowa
def distance(e1, e2):
    #uzupełnij tutaj


#Miara Manhattan
def distance2(e1,e2):
    #uzupełnij tutaj


group = {
    'A' : [(10, 1), (7, 6)],
    'B' : [(3, 1), (5, 4), (9,4)]
}
newEl = (8, 2)

dist = []
for gr, elems in group.items():
    for elem in elems:
        dist.append((gr, distance(newEl, elem)))

dist2 = []
for gr, elems in group.items():
    for elem in elems:
        dist2.append((gr, distance2(newEl, elem)))

k = 3
dist.sort(key=operator.itemgetter(1))
k_nearest = dist[:k]

dist2.sort(key=operator.itemgetter(1))
k_nearest2 = dist2[:k]

occur = {}
for element in k_nearest:
    nearGroup = element[0]
    if nearGroup in occur.keys():
        occur[nearGroup] += 1
    else:
        occur[nearGroup] = 1

occur2 = {}
for element in k_nearest2:
    nearGroup = element[0]
    if nearGroup in occur2.keys():
        occur2[nearGroup] += 1
    else:
        occur2[nearGroup] = 1

classif = max(occur, key=occur.get)
print("Euklides:")
print("Nowy element należy do grupy ", classif)

classif2 = max(occur2, key=occur2.get)
print("Manhattan:")
print("Nowy element należy do grupy ", classif2)