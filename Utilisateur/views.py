from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Client, Professeur
from .crypt import PasswordCrypto
from django.contrib.auth import authenticate, login

def accueil(request):
    if 'id_client' not in request.session:
        return HttpResponse("Accès non autorisé")
    
    return render(request, 'Client/accueil.html')

def deconnexion_client(request):
    if 'id_client' in request.session:
        del request.session['id_client']
        return redirect('connexion_client')
    return redirect('connexion_view')

def inscription_client_view(request):
    return render(request, 'Client/inscription_client.html')

def inscription_client(request):
    crypto = PasswordCrypto()
    
    if request.method == 'POST':
        nom = request.POST.get('nom')
        nom_majuscule = nom.upper()
        prenom = request.POST.get('prenom')
        date_de_naissance = request.POST.get('date_de_naissance')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        confirm_password = request.POST.get('confirm_password')
        numero_cin = request.POST.get('numero_cin')
        photo_profil = request.FILES.get('photo_profil')

        # Vérification des mots de passes
        if mot_de_passe != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'Client/inscription_client.html')

        # Vérification si l'email ou le CIN existe déjà
        if Client.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, 'Client/inscription_client.html')

        if Client.objects.filter(numero_cin=numero_cin).exists():
            messages.error(request, "Ce numéro de CIN est déjà utilisé.")
            return render(request, 'Client/inscription_client.html')

        try:
            
            encrypted_password = crypto.encrypt(mot_de_passe)
            
            # Enregistrement du client
            client = Client(
                nom=nom_majuscule,
                prenom=prenom,
                date_de_naissance=date_de_naissance,
                email=email,
                mot_de_passe=encrypted_password,  
                numero_cin=numero_cin,
                photo_profil=photo_profil
            )
            client.full_clean()  # Valide les contraintes du modèle
            client.save()
            #messages.success(request, "Inscription réussie !")
            return redirect('connexion_view')
            
        except ValidationError as e:
            messages.error(request, f"Erreur lors de l'inscription: {e}")
        except Exception as e:
            messages.error(request, f"Erreur lors du chiffrement du mot de passe: {str(e)}")

    return render(request, 'Client/inscription_client.html')

def connexion_view(request):
    return render(request, 'Client/connexion_client.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def connexion_client(request):
    crypt = PasswordCrypto()
    if request.method == 'POST':
        email = request.POST.get('email')
        mot_de_passe_clair = request.POST.get('mot_de_passe')
        mot_de_passe = crypt.encrypt(mot_de_passe_clair)
        # Authentification du client
        try:
            client = Client.objects.get(email=email, mot_de_passe=mot_de_passe)
            request.session['id_client'] = client.id_client
            return redirect('accueil')  # Redirige vers la page d'accueil du client
        except Client.DoesNotExist:
            messages.error(request, "Email ou mot de passe incorrect.")
            return render(request, 'Client/connexion_client.html')
    
    # Si la méthode n'est pas POST, afficher la page de connexion
    return render(request, 'Client/connexion_client.html')

def inscription_prof_view(request):
    return render(request, 'Professeur/inscription_prof.html')

def inscription_prof(request):
    crypto = PasswordCrypto()
    
    if request.method == 'POST':
        nom = request.POST.get('nom')
        nom_majuscule = nom.upper()
        prenom = request.POST.get('prenom')
        date_de_naissance = request.POST.get('date_de_naissance')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        confirm_password = request.POST.get('confirm_password')
        numero_cin = request.POST.get('numero_cin')
        photo_profil = request.FILES.get('photo_profil')
        biographie = request.POST.get('biographie')

        # Vérification des mots de passe
        if mot_de_passe != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'Professeur/inscription_prof.html')

        # Vérification si l'email ou le CIN existe déjà
        if Professeur.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, 'Professeur/inscription_prof.html')

        if Professeur.objects.filter(numero_cin=numero_cin).exists():
            messages.error(request, "Ce numéro de CIN est déjà utilisé.")
            return render(request, 'Professeur/inscription_prof.html')

        try:
            encrypted_password = crypto.encrypt(mot_de_passe)
            
            # Enregistrement du professeur
            professeur = Professeur(
                nom=nom_majuscule,
                prenom=prenom,
                date_de_naissance=date_de_naissance,
                email=email,
                mot_de_passe=encrypted_password,  
                numero_cin=numero_cin,
                photo_profil=photo_profil,
                biographie=biographie
            )
            professeur.full_clean()  # Valide les contraintes du modèle
            professeur.save()
            
            return redirect('connexion_view')
            
        except ValidationError as e:
            messages.error(request, f"Erreur lors de l'inscription: {e}")
        except Exception as e:
            messages.error(request, f"Erreur lors du chiffrement du mot de passe: {str(e)}")

    return render(request, 'Professeur/inscription_prof.html')

