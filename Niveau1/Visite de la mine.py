nb = int(input())
tab = []
for i in range(nb):
    tab.append(int(input()))
for i in range(nb-1, -1, -1):
    if tab[i] == 1 :
        print("2")
    elif tab[i] == 2 :
        print("1")
    elif tab[i] == 3 :
        print("3")
    elif tab[i] == 4 :
        print("5")
    else: 
        print("4")