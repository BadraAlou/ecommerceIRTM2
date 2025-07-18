from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

#from gestionNotes.noteapp.models import *
from boutique.models import *

from .serializers import *

class ProduitListView(generics.ListCreateAPIView):
    """
    API pour la création d'un etudiant et la recuperation de
    la liste des étudiant(avec la possibilité de filtrer
     par matricule).
    """
    queryset = Produit.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('nom',)

