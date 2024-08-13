
ancienTax = float(input())
nvTax = float(input())
ancienPrix = float(input())

prixHT = ancienPrix / (1 + (ancienTax / 100))
nvprix = prixHT * (1 + (nvTax/100))

prixEnCentime = nvprix * 100
roundPrix = round(prixEnCentime)
print (roundPrix / 100)
