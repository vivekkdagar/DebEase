# Homepage/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.run_page, name="run_page"),
]
