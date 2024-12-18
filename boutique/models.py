from django.db import models
from datetime import datetime

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50, blank=True)
    adresse = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - Client: {self.id}"
    
    
    
class Produit(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    #prix = models.DecimalField(max_digits=10, decimal_places=2)
    prix = models.PositiveIntegerField()
    image = models.ImageField(upload_to='imagesProduit', blank=True)

    def __str__(self):
        return f"{self.nom}"



class Commande(models.Model):

    #date = models.DateTimeField(default=datetime.now)
    date = models.DateField(default=datetime.now)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    #prix = models.IntegerField() 
    quantite = models.PositiveIntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


 