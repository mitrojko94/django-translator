from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Publish"))  #Proizvoljna varijabla koja sadrzi torku sa nasim zahtevima, 0 ili 1

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)  #Kad objavimo neki post, izbacuje nam se trenutno vreme objave, tome sluzi auto_now_add=True
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  #Parametar on_delete govori sta se desava sa korisnikom kada se izbrise iz baze podataka
    status = models.IntegerField(choices=STATUS, default=0)  #Napravio sam ovo polje koje ima izbor da bira, da li ce vrednost na izlazu biti o ili 1(to sam uradio pomocu varijable u kojoj sam definisao to)
    
    def __str__(self):
        return self.title
        