'''
Created on Sept 17, 2018

@author: Micha
'''

from apps.home.models import Veteran,User,Partner

from django.forms.models import ModelForm

class VeteransSignUp2(ModelForm):
    
    class Meta:
        model=Partner
        exclude = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
