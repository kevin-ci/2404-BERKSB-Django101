from django.urls import path
from . import views

urlpatterns = [
    path("view/<article_id>", views.show_article, name="read"),
    path("", views.show_homepage, name="home"),
]