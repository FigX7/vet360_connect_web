'''
Created on Apr 5, 2018

@author: Micha
'''

from django.contrib import admin
from django.urls import path
from .views import Home


urlpatterns = [
    path(r'',Home,name ='home'),
    ]
