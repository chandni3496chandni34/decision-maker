"""
URL configuration for crypto_decision_maker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.urls import path,include
# crypto/urls.py




urlpatterns = [
    path('admin/', admin.site.urls),
    path('crypto/', include('crypto.urls'),)
]'''
# crypto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crypto_decision_maker, name='crypto_decision_maker'),
]


