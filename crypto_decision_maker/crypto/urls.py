'''# crypto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.crypto_decision_maker, name='crypto_decision_maker'),
]'''
from django.contrib import admin
from django.urls import path,include
# crypto/urls.py




urlpatterns = [
    path('admin/', admin.site.urls),
    path('crypto/', include('crypto.urls')),
    path('api/', include('custom_api.urls')),
]