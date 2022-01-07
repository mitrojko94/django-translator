from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView):  #Stavio sam DetailView, jer ta klasa ima as_view() potreban za urls.py. A sve te klase su deo klase View. Ova klasa zahteva model(bazu podataka)
    model = Post
    template_name = "blog.html"


class PostList(generic.ListView):  #Prikazuje vise redova i zahteva query_set varijablu, sto je u ovom slucaju Post(baza podataka)
    queryset = Post.objects.filter(status=1).order_by("date_created")  #Mogao sam da stavim i Post.objects.all() onda izbacuje sve rezultate koje imamo, a kad sam stavio filter onda filtriram rezultate sa parametrom koji stavim u zagradu. Takodje, mogu da ih grupisem po necemu(order_by) i u zagradi stavim parametar po cemu ih grupisem(tipa "date_created"). Ovako su mi poredjani tako da je najnoviji post prvi, a da idem obrnuto, samo stavim "-date_created"
    template_name = "index.html"


class AboutView(generic.TemplateView):  #Koristim TemplateView, jer je u pitanju obican text, nema model(baze podataka). Samo koristim render_template, da vratim html kod
    template_name = "about.html"