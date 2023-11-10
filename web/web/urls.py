# web/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('Homepage.urls')),
]
