'''
Created on Apr 5, 2018

@author: Micha
'''
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(r'',views.PartnerLogged,name ='partLogged'),
    
    ]
