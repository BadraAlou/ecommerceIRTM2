from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    nomPersonne = "Maiga"
    agePersonne = 16
    classes = ['BBA1 IRT', 'BBA2 IRT', 'BBA3 IRT']
    valeurs = {'nom': nomPersonne, 'age': agePersonne, 'classes': classes}
    return render(request, 'boutique/index.html', context=valeurs)

def produit(request):
    produits = Produit.objects.all()
    return render(request, 'boutique/produit.html', {'produits': produits})