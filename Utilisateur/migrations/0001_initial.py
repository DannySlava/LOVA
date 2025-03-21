# Generated by Django 5.1.6 on 2025-02-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_de_naissance', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=128)),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('numero_cin', models.CharField(max_length=20, unique=True)),
                ('photo_profil', models.ImageField(blank=True, null=True, upload_to='photos_profil/')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id_professeur', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_de_naissance', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=128)),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('numero_cin', models.CharField(max_length=20, unique=True)),
                ('photo_profil', models.ImageField(blank=True, null=True, upload_to='photos_profil/')),
                ('biographie', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
