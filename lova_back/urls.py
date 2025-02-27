from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utilisateur/', include('Utilisateur.urls')),  # Assure-toi de respecter la casse correcte
]
