'''
Created on Sept 17, 2018

@author: Micha
'''

from apps.home.models import Veteran,User

from django.forms.models import ModelForm

class VeteransSignUp2(ModelForm):
    
    class Meta:
        model=Veteran
        exclude = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
