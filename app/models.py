from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.


class Position(models.Model):
    commune = models.CharField(max_length=25, null=False)
    adresse = models.CharField(max_length=25 , primary_key=True, null=False)
    
    Wilaya = (
        ("Adrar", "Adrar"),
        ("chlef", "chlef"),
        ("Laghouat", "Laghouat"),
        ("Oum-El-bouaghi", "Oum-El-bouaghi"),
        ("Batna", "Batna"),
        ("Bejaia", "Bejaia"),
        ("Biskra", "Biskra"),
        ("Bechar", "Bechar"),
        ("Blida", "Blida"),
        ("Bouira", "Bouira"),
        ("Tamanrasset", "Tamanrasset"),
        ("Tebessa", "Tebessa"),
        ("Tlemcen", "Tlemcen"),
        ("Tiaret", "Tiaret"),
        ("Tizi-Ouzou", "Tizi-Ouzou"),
        ("Alger", "Alger"),
        ("Djelfa", "Djelfa"),
        ("Jijel", "Jijel"),
        ("Setif", "Setif"),
        ("Saida", "Saida"),
        ("Skikda", "Skikda"),
        ("Sidi-Bel-Abbes", "Sidi-Bel-Abbes"),
        ("Annaba", "Annaba"),
        ("Guelma", "Guelma"),
        ("Constantine", "Constantine"),
        ("Medea", "Medea"),
        ("Mostaganem", "Mostaganem"),
        ("M-Sila", "M-Sila"),
        ("Mascara", "Mascara"),
        ("Ouargla", "Ouargla"),
        ("Oran", "Oran"),
        ("El-Bayadh", "El-Bayadh"),
        ("Illizi", "Illizi"),
        ("B-B-Arreridj", "B-B-Arreridj"),
        ("Boumerdes", "Boumerdes"),
        ("El-Tarf", "El-Tarf"),
        ("Tindouf", "Tindouf"),
        ("Tissemsilt", "Tissemsilt"),
        ("El-Oued", "El-Oued"),
        ("Khenchela", "Khenchela"),
        ("Souk-Ahras", "Souk-Ahras"),
        ("Tipaza", "Tipaza"),
        ("Mila", "Mila"),
        ("Ain-Defla", "Ain-Defla"),
        ("Naama", "Naama"),
        ("Ain-temouchent", "Ain-temouchent"),
        ("Ghardaia", "Ghardaia"),
        ("Relizane", "Relizane"),
        ("Timimoun", "Timimoun"),
        ("B-B-Mokhtar", "B-B-Mokhtar"),
        ("Ouled-Djellal", "Ouled-Djellal"),
        ("Beni-Abbes", "Beni-Abbes"),
        ("In-Salah", "In-Salah"),
        ("In-Guezzam", "In-Guezzam"),
        ("Touggourt", "Touggourt"),
        ("Djanet", "Djanet"),
        ("M-Ghair", "M-Ghair"),
        ("El-Meniaa", "El-Meniaa")

    )
    wil = models.CharField(max_length=50 , choices= Wilaya , null=False )
    
    def __str__(self):
        return self.adresse


class Client(models.Model):
    email = models.TextField(max_length=35 , null=False , primary_key=True)
    nom = models.CharField(max_length=25 , null=False)
    prenom = models.CharField(max_length=25 , null=False)
    telephone = models.IntegerField( null=False)
    
class Annonce(models.Model):
    
    Aonnonce_Type = (
        ("T" , "Terrain"),
        ("TA" , "Terrain Agricole"),
        ("A" , "Appartement"),
        ("M" , "Maison"),
        ("B" , "Bungalow")
    )
    
    Categorie = (
        ("V", "Vente"),
        ("E", "Echange"),
        ("L", "Location"),
        ("LV", "Location pour vacance")
    )
    annonceID = models.AutoField(auto_created=True,primary_key=True , null=False)
    categories = models.CharField(max_length=50 , choices= Categorie , null=False)
    types = models.CharField(max_length=50 , choices= Aonnonce_Type, null=False)
    surface = models.FloatField(null=False)
    prix = models.IntegerField(null=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    client = models.ForeignKey(Client , on_delete=models.CASCADE , null=False )
    pos = models.OneToOneField(Position, on_delete=models.CASCADE  , null=False)
    
    
    def __str__(self):
        return self.description
    
class Photo(models.Model):
    photoID = models.AutoField(auto_created=True,primary_key=True , null=False)
    image = models.ImageField()
    annonce = models.ForeignKey(Annonce , on_delete=models.CASCADE , null=False)
    def __str__(self):
        return self.image
    
class Message(models.Model):
    messageID = models.AutoField(auto_created=True,primary_key=True , null=False)
    annonce = models.ForeignKey(Annonce , on_delete=models.CASCADE , null=False)
    client = models.ForeignKey(Client , on_delete=models.CASCADE , null=False )
    description = models.TextField(null=False)
    