'''
Created on Sept 17, 2018

@author: Micha
'''

from apps.home.models import Veteran,User,Partner

from django.forms.models import ModelForm
from django import forms


class PartnerInfoForm(forms.Form):
    
    partner_web_address = forms.CharField(help_text = "Web Address")
        
