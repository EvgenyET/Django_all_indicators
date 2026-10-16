"""Django_all_indicators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from App.newapp import page1
from App.views import page
from App.app2 import page2
from App.app3 import page3

urlpatterns = [
    path('', page, name='home'),
    path('btc_chart', page1, name='page1'),
    path('fear_and_greed_index', page2, name='page2'),
    path('ema_strategy', page3, name='page3'),
]