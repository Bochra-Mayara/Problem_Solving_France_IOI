n = int(input())
TotalEquipe1Final = 0
TotalEquipe2Final = 0
for i in range(n):
    TotalEquipe1Tour = int(input())
    TotalEquipe2Tour = int(input())
    TotalEquipe1Final +=  TotalEquipe1Tour
    TotalEquipe2Final +=  TotalEquipe2Tour
if(TotalEquipe1Final > TotalEquipe2Final ):
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 : " + str(TotalEquipe1Final ))
print("Poids total pour l'équipe 2 : " + str(TotalEquipe2Final ))