'''
Created on Apr 5, 2018

@author: Micha
'''
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    url(r'getLocation',views.getLocation,name ='getLocationAll'),
    url(r'getGeocode',views.getGeocode,name ='getGeocode'),
    url(r'setPartnerPos',views.setPartnerPos,name ='setPartnerPos'),
    ]
