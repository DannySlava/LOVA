from django.contrib import admin

# Register your models here.
from .models import Specialite, Cours

admin.site.register(Specialite)
admin.site.register(Cours)