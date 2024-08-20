
np = int(input())
p = int(input())
tab = []
for i in range(np):
    tab.append(int(input()))
for i in range(p):
    a = int(input())
    b = int(input())
    tab[a],tab[b] = tab[b],tab[a]
for i in range(np):
    print(tab[i])
