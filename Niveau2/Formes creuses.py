#Définiton de la fonction ligne
def DessinLigne(taille):
   for i in range(taille):
      print("X", end="")
   print()
  
#Définition de la fonction rectangle
def DessinRectangle(lignes, colonnes):
   for iLig in range(lignes):
        #dessin de la première et de la dernière ligne du rectangle : ligne "pleine"
        if iLig==0 or iLig==lignes-1:
            for iCol in range(colonnes):
                print("#",end="")
            print()
        #dessin des lignes "vides" du rectangle, entre la première et la dernière
        elif iLig>0 and iLig<lignes-1:
            print("#",end="")
            if colonnes==1:
               print()
            else:
               for iCol in range(1,colonnes-1):
                   print(" ",end="")
               print("#")
               
#Définition de la fonction Triangle
def dessinTriangle(hauteur):
   esp=0
   #sommet du triangle
   print("@")
   #lignes 1 à hauteur-1:
   for iLig in range(1,hauteur-1):
      print("@",end="")
      for iCol in range(esp):
         print(" ",end="")
      print("@")
      esp=esp+1
   for iCol in range(hauteur):
      print("@",end="")

taille=int(input())
DessinLigne(taille)
print()

lignes=int(input())
colonnes=int(input())
DessinRectangle(lignes, colonnes)
print()

hauteur=int(input())
dessinTriangle(hauteur)