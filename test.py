"""
print("Hello world")
a = 3
b = 2
print(a)
print(a+b)
"""

#print(f"la valeur de a est : {a} et la valeur de b est : {b}")

"""
print(a**b) 
print(a//b)

if a > b:
    print("A est superieur a b")

elif b > a:
    print("B est superieur a a")
    
else:
    print("A et b sont egales")

print(range(10))
for i in range(10):
    print(i)
"""
"""
noms = ["Camara", 'Keita', 'Diallo']
for nom in noms:
    print(nom)

i = 1
while i < 10:
    print(i)
    i = i +1
"""

"""

def somme(a=1, b=1):
    return a + b

def bonjour():
    print("Bonjour")

x = somme()

print(x)
bonjour()  # Appel de la fonction bonjour() 

"""

class Vehicule:
    def __init__(self, marqueP, modeleP, anneeP):
        self.marque = marqueP
        self.modele = modeleP
        self.annee = anneeP

    def getMarque(self):
        return self.marque
    
    def setMarque(self, nouvelleMarque):
        self.marque = nouvelleMarque


v = Vehicule(marqueP="Mercedes", modeleP="190", anneeP=1990)
print(v.marque)
v.marque = "Toyota"
print(v.getMarque())
v.setMarque("Honda")
print(v.getMarque())


# definit une class VoitureElectrique
class VoitureElectrique(Vehicule):
    def __init__(self, marqueP, modeleP, anneeP, autonomieP):
        super().__init__(marqueP, modeleP, anneeP)
        self.autonomie = autonomieP

vehiculeElectric = VoitureElectrique(marqueP="Mercedes AMG", modeleP="AMG", anneeP=2020, autonomieP="500 KM")
print(vehiculeElectric.autonomie)  # Affiche 500 KM
print(vehiculeElectric.getMarque())  # Affiche Mercedes AMG