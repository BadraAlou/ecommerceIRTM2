from django.contrib import admin
from django.utils.html import format_html

from .models import *

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','nom', 'prenom']
    list_filter = ('nom', 'prenom')
    search_fields = ('nom', 'prenom')
    

class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'displayImage',]
    list_filter = ('nom', 'prix')

    def displayImage(self, obj):
        try:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        except:
            return "Pas D'image disponible"
        
        
    
    displayImage.short_description = 'Image du produit'



class CommandeAdmin(admin.ModelAdmin):
    list_display = ['date', 'produit', 'quantite', 'client', 'montant']
    list_filter = ('date', 'client')

    
    def montant(self, obj):
        return obj.produit.prix * obj.quantite
    


    

admin.site.register(Client, ClientAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(Produit, ProduitAdmin)
