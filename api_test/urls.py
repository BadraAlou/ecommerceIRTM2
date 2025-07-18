from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from .views import *


urlpatterns = [
    path('', include(router.urls)),
    path('produits', ProduitListView.as_view(), name='produits_list_api'),
    
]

