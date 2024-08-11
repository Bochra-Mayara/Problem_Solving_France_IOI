def Plan(mp, p):
    if (mp >= p) and (mp - p <= 50):
        return True
    elif (mp < p) and (p - mp <= 50):
        return True
    else:
        return False
    
maposition = int(input("Saisissez votre position: " ))
nbVillages = int(input("Saisissez le nombre de villages: "))

nbVResult = 0
for i in range(nbVillages):
    positionVillage = int(input("Saisissez la position du village:"))
    if(Plan(maposition,positionVillage)):
        nbVResult += 1
print("Nombre de villages à moins ou égal à 50 km:" , nbVResult)
