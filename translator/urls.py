from . import views
from django.urls import path

urlpatterns = [
    path("", view=views.translator_view, name="translator_view"),  #Znaci da ce me ovaj URL odvesti pravo na localhost:8000/translate
]
