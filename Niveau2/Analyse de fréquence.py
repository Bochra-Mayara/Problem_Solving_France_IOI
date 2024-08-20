
nbLignes, nbMots = map(int, input().split())


tab = [0] * 101


for i in range(nbLignes):
    mots = input().split()
    for mot in mots:
        longueur = len(mot)
        tab[longueur] += 1


for i in range(1, 101): 
    if tab[i] > 0:
        print("{} : {}".format(i, tab[i]))
