from django.urls import path
from . import views

urlpatterns = [
    path('accueil-client/', views.accueil_client, name='accueil_client'),
    path('deconnexion-client/', views.deconnexion_client, name='deconnexion_client'),


    path('client/inscription', views.inscription_view, name='inscription_view'),
    path('inscription/', views.inscription, name='inscription_client'),

    path('client/connexion', views.connexion_view, name='connexion_view'),
    path('connexion/', views.connexion, name='connexion_client'),
]