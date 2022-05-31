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
def odleglosc(e1, e2):
    #uzupełnij tutaj


#Miara Manhattan
def odleglosc2(e1,e2):
    #uzupełnij tutaj


grupa = {
    'A' : [(10, 1), (7, 6)],
    'B' : [(3, 1), (5, 4), (9,4)]
}
nowy = (8, 2)

odl = []
for gr, elems in grupa.items():
    for elem in elems:
        odl.append((gr, odleglosc(nowy, elem)))

odl2 = []
for gr, elems in grupa.items():
    for elem in elems:
        odl2.append((gr, odleglosc2(nowy, elem)))

k = 3
odl.sort(key=operator.itemgetter(1))
k_najblizszych = odl[:k]

odl2.sort(key=operator.itemgetter(1))
k_najblizszych2 = odl2[:k]

wyst = {}
for element in k_najblizszych:
    naj_grupa = element[0]
    if naj_grupa in wyst.keys():
        wyst[naj_grupa] += 1
    else:
        wyst[naj_grupa] = 1

wyst2 = {}
for element in k_najblizszych2:
    naj_grupa = element[0]
    if naj_grupa in wyst2.keys():
        wyst2[naj_grupa] += 1
    else:
        wyst2[naj_grupa] = 1

klasyfikacja = max(wyst, key=wyst.get)
print("Euklides:")
print("Nowy element należy do grupy ", klasyfikacja)

klasyfikacja2 = max(wyst2, key=wyst2.get)
print("Manhattan:")
print("Nowy element należy do grupy ", klasyfikacja2)