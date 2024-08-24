# Constantes de conversion
METERS_TO_FEET = 3.28084
GRAMS_TO_POUNDS = 0.002205
FAHRENHEIT_OFFSET = 32
FAHRENHEIT_MULTIPLIER = 1.8

# Nombre de conversions
n = int(input())

# Traitement des conversions
for _ in range(n):
    valeur, unite = input().split()
    valeur = float(valeur)
    
    if unite == "m":
        resultat = valeur * METERS_TO_FEET
        print("{:.6f} p".format(resultat))
    elif unite == "g":
        resultat = valeur * GRAMS_TO_POUNDS
        print("{:.6f} l".format(resultat))
    elif unite == "c":
        resultat = FAHRENHEIT_OFFSET + FAHRENHEIT_MULTIPLIER * valeur
        print("{:.6f} f".format(resultat))
