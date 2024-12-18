from django.shortcuts import render

# Create your views here.
def index(request):
    nomPersonne = "Maiga"
    valeurs = {'nom': nomPersonne}
    return render(request, 'boutique/index.html', context=valeurs)

def produit(request):
    return render(request, 'boutique/produit.html')