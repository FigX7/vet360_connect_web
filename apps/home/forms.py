'''
Created on May 11, 2018

@author: Micha
'''

    
from django import forms
from django.db import transaction
from .models import Veteran, User, Partner
from django.contrib.auth.forms import UserCreationForm


class VeteranSignUpForm(UserCreationForm):
    
    
    email = forms.EmailField(required=True)
    class Meta:
        model = Veteran
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.isVet = True
        if commit:
            user.save()
        return user    
class VetLoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class PartnerSignUpForm(UserCreationForm):
    
   email = forms.EmailField(required=True)
   class Meta:
        model = Partner
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
   def save(self, commit=True):
        user = super().save(commit=False)
        user.isPart = True
        if commit:
            user.save()
        return user    
    

class PartnerLoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
                