"""wms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from .models import Task
from . import views

urlpatterns = [
    path('', views.operations, name ='operations'),
    path('order/create/', views.order_create, name='order_create'),
    path('orders/', views.orders, name='orders'),
    path('material-autocomplete', views.MaterialAutocomplete.as_view(),
                      name='material-autocomplete',
                  ),
    #path('order/<int:id>/', views.operations, name='operations'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
