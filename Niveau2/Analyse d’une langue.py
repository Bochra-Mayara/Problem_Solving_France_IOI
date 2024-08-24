recherche = input()
nbLignes = int(input())
s = 0
for i in range(nbLignes):
    ligne = input()
    for char in ligne:
        if char == recherche:
            s += 1
print(s)