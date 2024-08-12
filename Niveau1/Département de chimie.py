nTotal = int(input())
tempMin = int(input())
tempMax = int(input())

for i in range(nTotal):
    t = int(input())
    if t < tempMin or t > tempMax:
        print("Alerte !!")
        break
    else:
        print("Rien à signaler ")
