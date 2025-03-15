from django.db import models                                                                                                                                               
from Utilisateur.models import Professeur
from django.db import models

# Create your models here.

class Specialite(models.Model):
    id_specialite = models.AutoField(primary_key=True)
    nom_specialite = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='specialite')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_specialite

    def get_id_specialite(self):
        return self.id_specialite

    def get_nom_specialite(self):
        return self.nom_specialite
    
    def get_description(self):
        return self.description
    
    def get_image(self):
        return self.image
    
    def get_date_creation(self):
        return self.date_creation
    
    def set_nom_specialite(self, nom_specialite):
        self.nom_specialite = nom_specialite
    
    def set_description(self, description):
        self.description = description

    def set_image(self, image):
        self.image = image

    def set_date_creation(self, date_creation):
        self.date_creation = date_creation


class Cours(models.Model):
    id_cours = models.AutoField(primary_key=True)
    id_professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    id_specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    prix_heure = models.FloatField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cours {self.id_cours} - {self.id_professeur}"


    def get_id_cours(self):
        return self.id_cours

    def get_id_professeur(self):
        return self.id_professeur
    
    def get_id_specialite(self):
        return self.id_specialite
    
    def get_prix_heure(self):
        return self.prix_heure
    
    def get_date_creation(self):
        return self.date_creation

    def set_id_professeur(self, id_professeur):
        self.id_professeur = id_professeur