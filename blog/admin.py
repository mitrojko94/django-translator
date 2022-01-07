from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "author")  #Ovde stavim koja polja iz baze zelim da prikazem u admin-u


# Register your models here.
admin.site.register(Post, PostAdmin)