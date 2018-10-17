'''
Created on Apr 5, 2018

@author: Micha
'''

from django.contrib import admin
from django.urls import path
from .views import VetProfile


urlpatterns = [
    path(r'',VetProfile,name ='vetProfile'),
    ]
