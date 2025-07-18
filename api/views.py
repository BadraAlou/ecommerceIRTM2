from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from boutique.models import *
from .serializers import *

class ProduitListView(generics.ListCreateAPIView):
    """
    API permettant de récuperer la liste des produits dans la base de données
    """
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('nom', )
