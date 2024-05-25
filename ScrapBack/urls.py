"""
URL configuration for ScrapBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views.scrappers_views import Scrappy
from .views.user_views import Auth
from .views.test import TestView
#hola
urlpatterns = [
    # path('tienda/<str:producto>/',Scrappy.alcampo), ESTO ES GET
    path('all/<str:producto>/',Scrappy.all_scrappers),
    path('makro/<str:producto>/',Scrappy.makro),
    path('carrefour/<str:producto>/',Scrappy.carrefour),
    path('eci/<str:producto>/',Scrappy.eci),
    path('alcampo/<str:producto>/',Scrappy.alcampo),
    path('auth/login',Auth.login),
    path('auth/register',Auth.register),
    path('auth/forgotpassw',Auth.forgotPassw),
    path('auth/changepassw',Auth.changePassw),
    path('auth/authtoken',Auth.authToken),
    path('test',TestView.get),
]

    