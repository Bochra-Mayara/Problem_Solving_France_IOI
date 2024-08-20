nb = int(input())
lmax = 0
for i in range(nb):
    a = input()
    if len(a) > lmax:
        lmax = len(a)
        print(a)