from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("edit/<int:pk>", views.edit, name="edit"),
]
