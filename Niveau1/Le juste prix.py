nb = int(input("Entrez le nombre de marchands: "))
tab = []

for i in range(nb):
    tab.append(int(input()))
    
min = tab[0]
indicePrix = 1
for i in range(1, nb):
    if tab[i] <= min:
        min = tab[i]
        indicePrix = i +1
print(indicePrix)
