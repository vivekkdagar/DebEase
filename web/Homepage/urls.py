# your_project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="run_page"),
]
