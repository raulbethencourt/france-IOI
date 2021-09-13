#    ______                                 ________  ____
#   / ____/________ _____  ________        /  _/ __ \/  _/
#  / /_  / ___/ __ `/ __ \/ ___/ _ \______ / // / / // /
# / __/ / /  / /_/ / / / / /__/  __/_____// // /_/ // /
#/_/   /_/   \__,_/_/ /_/\___/\___/     /___/\____/___/
#
# Author:
#   Raul Bethencourt Gonzalez
#
# 2021 CarPa (https://raulbethencourt.com)
#

# 1.1.1
print("Hello people!")

# 1.1.2
print("Coucou !")
print("Je m'appelle Camthalion")
print("Ma devise est 'Parler peu mais parler bien'.")

# 1.1.3
print("Tout droit tu grimperas,")
print("La clé tu trouveras,")
print("Habile tu seras,")
print("Quand tu les porteras,")
print("Et avec le chef tu reviendras !")

# 1.1.4
from robot import *

haut()
haut()
haut()
droite()
droite()
bas()
bas()
droite()

# 1.1.5
from robot import *

deplacer(1, 3)
deplacer(1, 2)
deplacer(3, 2)
deplacer(1, 3)
deplacer(2, 3)
deplacer(2, 1)
deplacer(3, 2)
deplacer(1, 3)
deplacer(2, 3)
deplacer(1, 2)
deplacer(3, 2)
deplacer(3, 1)
deplacer(2, 1)
deplacer(3, 2)
deplacer(1, 3)
deplacer(1, 2)
deplacer(3, 2)
deplacer(2, 1)
deplacer(2, 3)
deplacer(1, 3)
deplacer(2, 1)
deplacer(3, 2)
deplacer(3, 1)
deplacer(2, 1)
deplacer(2, 3)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 1)
deplacer(3, 2)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 1)
deplacer(2, 3)
deplacer(1, 3)

# 1.1.6
from robot import *

remplir(5)
transferer(5, 3)
vider(3)
transferer(5, 3)
remplir(5)
transferer(5, 3)

# 1.2.1
for loop in range(135):
   print("Je dois respecter le Grand Sorcier.")

# 1.2.2
for loop in range(13):
   print("9 * 8 = 72")

# 1.2.4
from robot import *

for loop in range(21):
   haut()
   droite()
for loop in range(21):
   gauche()
   bas()

# 1.2.5
for loop in range(30):
   print("a_", end = "")
print()
for loop in range(30):
   print("b_", end = "")
print()
for loop in range(30):
   print("c_", end = "")

# 1.2.6
for loop in range(20):
   for loop in range(20):
      print("OX", end = "")
   print()
   for loop in range(20):
      print("XO", end = "")
   print()

# 1.2.7
from robot import *

for loop in range(108):
   for loop in range(13):
      haut()
   for loop in range(13):
      droite()
   for loop in range(13):
      bas()
   for loop in range(13):
      gauche()

# 1.2.8
from robot import *

for loop in range(20):
   ramasser()
   for loop in range(15):
      droite()
   deposer()
   for loop in range(15):
      gauche()

# 1.2.9
from robot import *

haut()
for loop in  range(4):
   for loop in range(8):
      haut()
   droite()
   for loop in range(8):
      bas()
   droite()
for loop in range(8):
   haut()
droite()
for loop in range(8):
   bas()
bas()
for loop in range(9):
   gauche()

# 1.3.1
print(42)

# 1.3.2
print(12581 - 11937)

# 1.3.3
print((25 + 30 + 27 + 22 -8) * 3)

# 1.3.4
distance = 2 + 34 + 6
print(distance, end = " ")
print(2 * distance, end = " ")
print(3 * distance, end = " ")

# 1.3.5
distance = (5 * 17) + (2 * 7) + 5 + (2 * 2)
print(distance * distance, end = " ")
print(distance * 4)

# 1.3.6
constante = 1
print (constante)
for loop in range(99):
   print (constante + 1)
   constante = constante +1
print ("J'arrive !")

# 1.3.7
print("V")
print("V")
print("I")
print("I")
print("V")
print("I")
print("I")

# 1.3.8
decompte = 100
for loop in range (100):
   print(decompte)
   decompte = decompte - 1
print(0)
print("Décollage !")

# 1.3.9
crapauds = 1337
for loop in range (12):
   crapauds = crapauds + crapauds
print(crapauds)

# 1.3.10
totalBonbons = 0
numTir = 1
for loop in range(50):
   totalBonbons = totalBonbons + numTir
   print(totalBonbons)
   numTir = numTir + 1

# 1.3.11
from robot import *

for anneau in range(1,11):
   for loop in range(anneau):
      droite()
   ramasser()
   for loop in range(anneau):
      gauche()
   deposer()

# 1.3.12
nbCube = 1
coté = 1
total = 1

for loop in range (8):
   coté = coté + 2
   nbCube = coté*coté*coté
   total = total + nbCube
print(total)

# 1.3.13
for numero in range(1,21):
  for loop in range(1,21):
    total = numero * loop
    print(total," ", end = "")
  print()

# 1.4.1

