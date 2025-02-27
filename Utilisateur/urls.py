from django.urls import path
from . import views

urlpatterns = [
    path('accueil-client/', views.accueil, name='accueil'),
    path('deconnexion-client/', views.deconnexion_client, name='deconnexion_client'),

    path('client/inscription', views.inscription_view, name='inscription_view'),
    path('inscription_client/', views.inscription_client, name='inscription_client'),
    
    path('client/connexion', views.connexion_view, name='connexion_view'),
    path('connexion_client/', views.connexion_client, name='connexion_client'),

    path('professeur/inscription', views.inscription_prof_view, name='inscription_prof_view'),
    path('inscription_prof/', views.inscription_prof, name='inscription_prof'),

]