from django.db import models

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    date_inscription = models.DateTimeField(auto_now_add=True)
    numero_cin = models.CharField(max_length=20, unique=True)
    photo_profil = models.ImageField(upload_to='photos_profil/Client', null=True, blank=True)  

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    # Getters
    def get_id_client(self):
        return self.id_client

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_date_de_naissance(self):
        return self.date_de_naissance

    def get_email(self):
        return self.email

    def get_mot_de_passe(self):
        return self.mot_de_passe

    def get_date_inscription(self):
        return self.date_inscription

    def get_numero_cin(self):
        return self.numero_cin

    def get_photo_profil(self):
        return self.photo_profil

    # Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_date_de_naissance(self, date_de_naissance):
        self.date_de_naissance = date_de_naissance

    def set_email(self, email):
        self.email = email

    def set_mot_de_passe(self, mot_de_passe):
        self.mot_de_passe = mot_de_passe

    def set_numero_cin(self, numero_cin):
        self.numero_cin = numero_cin

    def set_photo_profil(self, photo_profil):
        self.photo_profil = photo_profil

class Professeur(models.Model):
    id_professeur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    date_inscription = models.DateTimeField(auto_now_add=True)
    numero_cin = models.CharField(max_length=20, unique=True)
    photo_profil = models.ImageField(upload_to='photos_profil/Professeur', null=True, blank=True)
    biographie = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    # Getters
    def get_id_professeur(self):
        return self.id_professeur

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_date_de_naissance(self):
        return self.date_de_naissance

    def get_email(self):
        return self.email

    def get_mot_de_passe(self):
        return self.mot_de_passe

    def get_date_inscription(self):
        return self.date_inscription

    def get_numero_cin(self):
        return self.numero_cin

    def get_photo_profil(self):
        return self.photo_profil

    def get_biographie(self):
        return self.biographie

    # Setters
    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_date_de_naissance(self, date_de_naissance):
        self.date_de_naissance = date_de_naissance

    def set_email(self, email):
        self.email = email

    def set_mot_de_passe(self, mot_de_passe):
        self.mot_de_passe = mot_de_passe

    def set_numero_cin(self, numero_cin):
        self.numero_cin = numero_cin

    def set_photo_profil(self, photo_profil):
        self.photo_profil = photo_profil

    def set_biographie(self, biographie):
        self.biographie = biographie
