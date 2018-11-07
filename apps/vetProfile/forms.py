'''
Created on Sept 17, 2018

@author: Micha
'''

from apps.home.models import Veteran,User
from django import forms
from django.core.exceptions import ValidationError
from localflavor.us.forms import USZipCodeField
from localflavor.us.forms import USStateSelect

class VeteransPersonalForm(forms.ModelForm):
    VET_BRANCH_CHOICES = (
        ('','---------'),
        ('usaf','Air Force'),
        ('usa', 'Army'),
        ('uscg', 'Coast Guard'),
        ('usmc', 'Marines'),
        ('usn', 'Navy'),
    )
    VET_BOOL_CHOICES = (
    ('','---------'),
    (True,'Yes'),
    (False, 'No'),

    
    )
    
    ava_user = forms.ImageField(required = False,label="Update Avatar")
    vet_branch = forms.ChoiceField(choices=VET_BRANCH_CHOICES, required = False,label="Branch:")
    
    vet_isPost911 = forms.ChoiceField(choices=VET_BOOL_CHOICES, required = False,label="Post 911 Veteran:")
    vet_isCombat = forms.ChoiceField(choices=VET_BOOL_CHOICES, required = False,label="Veteran Combat Action Award or Direct Combat Attachment:")
    vet_isNotifications = forms.ChoiceField(choices=VET_BOOL_CHOICES, required = False,label="Recieve Notifications:")
    vet_isShared = forms.ChoiceField(choices=VET_BOOL_CHOICES, required = False,label="Share Location: (Required To locate Fellow Veterans and Resources")
    vet_mobile = forms.CharField(required = False,label="Phone Number",help_text = "XXX-XXX-XXXX")
    vet_zip = USZipCodeField(required = False,label="Zip Code",help_text = "XXXXXX")
    
    class Meta:
    
        model=Veteran
        
        
        fields = (
                  'vet_branch',  
                  'vet_mobile', 
                  'vet_state',
                  'vet_zip',
                  'vet_unit',
                  'vet_isPost911',
                  'vet_isCombat',
                  'vet_isNotifications',
                  'vet_isShared',
                  'ava_user',
                  )
        
    
   
        
        
        