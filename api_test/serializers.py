
from rest_framework import serializers

from boutique.models import *


class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
        #fields = ['nom', 'prenom', 'niveau']



