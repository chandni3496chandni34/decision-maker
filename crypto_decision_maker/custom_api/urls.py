# custom_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cryptocurrency_data/', views.fetch_cryptocurrency_data, name='cryptocurrency_data'),
]
