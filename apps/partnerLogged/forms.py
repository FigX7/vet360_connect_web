'''
Created on Sept 17, 2018

@author: Micha
'''

from apps.home.models import Veteran,User,Partner
from localflavor.us.forms import USZipCodeField
from localflavor.us.forms import USStateSelect
from django.forms.models import ModelForm
from django import forms


class PartnerInfoForm(forms.ModelForm):
    partner_logo = forms.ImageField(required = False)
    
    class Meta:
        model = Partner
        fields = {
            
            'partner_phone',
            'partner_zip',
            'partner_address1',
            'partner_address2',
            'partner_mission',
            'partner_name',
            'partner_state',
            'partner_web_address',
            'partner_logo',
            }
class PartnerAddressForm(forms.ModelForm):
   
    class Meta:
        model = Partner
        fields = {
            
            
           
            'partner_address1',
            
            
            
            'partner_address2',
            'partner_zip',
            
            'partner_state',
            'partner_phone',
            }






#    {% elif field1 == formPart.partner_state %}
#                                 {{ field1.errors }}    
#                                 <div class="form-group">
#                                       <label for="sel1">{{ field1.label }}</label>
#                                       
#                                       <select name = "{{ field1.name }}">
#                                       {% for choice in formPart.partner_state.field.choices %}
#                                           {% if field1.value ==  choice.0 %}
#                                               <option selected value = "{{ choice.0 }}" >{{ choice.1 }}</option>
#                                           
#                                           
#                                           {% elif not field1.value  == choice.0 %}
#                                           <option  value = "{{ choice.0 }}" >{{ choice.1 }}</option>
#                                                   
#                                           {% endif %}
#                                       {% endfor %}
#                                       </select>
#                                 </div>   