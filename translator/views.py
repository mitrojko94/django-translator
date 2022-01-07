from django.shortcuts import render
from translator import translate
#from . import translate  #Ovo je drugi nacin da se imortuje translate


# Create your views here.

#Ova f-ja u pozadini ocekuje "request" i prosledjuje ga URL adresi, koja prosledjuje taj "request object" kada korisnik poseti sajt
def translator_view(request):
    if request.method == "POST":  #Proveravam da li je "request" POST
        original_text = request.POST["my_textarea"]  #Prosledim request.POST i kao parametar ide ime input polja gde kucam text, a to ime definisem u html kodu za translator
        #output = original_text.capitalize()  #Definisem proizvoljnu varijablu i prosledim joj nasu varijablu iznad sa nekom metodom(sta cu da uradim, tipa upper, lower i slicno)
        output = translate.translate(original_text)  #Pozvao sam metodu translate i prosledio joj metodu translate, kojoj kao parametar prosledjujem original_text, jer to menjam
        return render(request, "translator.html", {
            "output_text": output,
            "original_text": original_text  #Ovo sam uradio, da bih video originalan text
        })  #Prosledim render koji ima tri parametra(prvi je uvek request, drugi je html kod i treci je tipa key:value). U ovom slucaju key=proizvoljno_ime, a value=nasa varijabla iznad, sa metodom da nesto uradimo tekstu
    else:
        return render(request, "translator.html")  #Render ocekuje prvi parametar request, a drugi html kod





#Za translate koristim biblioteku googletrans, a ako ne radi ta verzija, koristim googletrans == 4.0.0-rc1
