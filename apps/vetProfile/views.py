
from django.shortcuts import render, redirect
from .forms import VeteransPersonalForm
from django.contrib import messages



#from django.core import serializers

# Create your views here.

def VetProfile(request):
    user = request.user.veteran
    data = {
    'vet_branch':user.vet_branch,  
    'vet_mobile':user.vet_mobile, 
    'vet_state':user.vet_state,
    'vet_zip':user.vet_zip,
    'vet_unit':user.vet_unit,
    'vet_isPost911':user.vet_isPost911,
    'vet_isCombat':user.vet_isCombat,
    'vet_isNotifications':user.vet_isNotifications,
    'vet_isShared':user.vet_isShared,
    'vet_isSignedUp':user.vet_isSignedUp,
    }
    
  
    if request.method == 'POST':
        
        user = request.user.veteran
        formPers = VeteransPersonalForm(request.POST,request.FILES,instance=user)
        context = {
                'formPers':formPers,
                'user':user,
            }
        
        if formPers.is_valid():
            formPers.save(commit=False)
            
            
            user.vet_isSignedUp = formPers.cleaned_data['vet_isShared']
            user.vet_unit = formPers.cleaned_data['vet_unit']
            formPers.save()
            
            return redirect("vetProfile")
        else:
            print(formPers.is_valid())
            print(formPers.errors)
            
            formPers = VeteransPersonalForm(request.POST,request.FILES,instance=user) 
            
            context = {
                'formPers':formPers,
                'user':user,
            }
            print(request.POST)
            return render(request,"vetProfile/vetProfile.html",context)
             
        
    else:
        user = request.user.veteran
        formPers = VeteransPersonalForm(data,initial=data)   
        
        context = {
                'formPers':formPers,
                'user':user,
            }
        
        return render(request,"vetProfile/vetProfile.html",context) 
    
    
