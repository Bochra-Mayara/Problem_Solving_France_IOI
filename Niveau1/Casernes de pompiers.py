nbPaire = int(input())
for i in range(nbPaire):
    xd0 = int(input())
    xf0 = int(input())
    yd0 = int(input())
    yf0 = int(input())
    xd1 = int(input())
    xf1 = int(input())
    yd1 = int(input())
    yf1  = int(input())
    if( xd1 >= xf0 or xd0 >= xf1 or yd1 >= yf0 or yd0 >= yf1 ):
        print("NON")
    else:
        print("OUI")