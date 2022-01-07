from .import views
from django.urls import path

urlpatterns = [
    path("<slug:slug>", view=views.BlogView.as_view(), name="blog_view"),
    path("", view=views.PostList.as_view(), name="home"),
    path("about/", view=views.AboutView.as_view(), name="about_view"),
]