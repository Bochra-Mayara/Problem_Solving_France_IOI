
nb = int(input())


tab = [0] * nb

for i in range(nb):
    a = int(input())
    tab[a] = i

for i in range(nb):
    print(tab[i])
