from django.urls import path
from . import views

urlpatterns = [
    path("view/<article_id>", views.show_article, name="read"),
    path("", views.show_homepage, name="home"),
    path("create/", views.create_article, name="create"),
    path("edit/<article_id>", views.edit_article, name="edit"),
    path("delete/<article_id>", views.delete_article, name="delete"),
]