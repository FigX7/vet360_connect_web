
from .forms import PartnerInfoForm,PartnerAddressForm
# Create your views here.
from django.shortcuts import render, redirect
from apps.home.models import Partner
def PartnerLogged(request):
    boolPartInfo = 'btn-PartInfo' in request.POST
    boolPartAddress = 'btn-PartAddress' in request.POST
    boolPartGeoCode ='btn-geocode' in request.POST
    print(boolPartInfo)
    print(boolPartAddress)
    print(boolPartGeoCode)
    user = request.user.partner
    data = {
        'partner_web_address':user.partner_web_address,
        'partner_state':user.partner_state,
        'partner_zip':user.partner_zip,
        'partner_phone':user.partner_phone,
        'partner_name':user.partner_name,
        'partner_address':user.partner_address,
        'partner_mission':user.partner_mission,
        
    }
    data2 = {
        
        'partner_state':user.partner_state,
        'partner_zip':user.partner_zip,
        'partner_phone':user.partner_phone,
        
        'partner_address':user.partner_address,
        
        
    }
    if request.method == 'POST' and boolPartInfo:
        print(request.POST)
        user = request.user.partner
        formPart = PartnerInfoForm(request.POST,request.FILES,instance=user)
        formPartAddress = PartnerAddressForm(data,initial=data2)
        context = {
                'formPart':formPart,
                'formPartAddress':formPartAddress,
                'user':user,
            }
        
        if formPart.is_valid():
            formPart.save(commit=False)
            
            
           
            formPart.save()
            
            return redirect("partnerLogged")
        else:
            print(formPart.is_valid())
            print(formPart.errors)
            
            formPart = PartnerInfoForm(request.POST,request.FILES,instance=user) 
            formPartAddress = PartnerAddressForm()
            context = {
                'formPart':formPart,
                'formPartAddress':formPartAddress,
                'user':user,
            }
            print(request.POST)
            return render(request,"partnerLogged/partnerLogged.html",context) 
             
    elif  request.method == 'POST' and boolPartAddress:
        user = request.user.partner
        formPart = PartnerInfoForm(data,initial=data)
        formPartAddress = PartnerAddressForm(request.POST,request.FILES,instance=user)
        context = {
                'formPart':formPart,
                'formPartAddress':formPartAddress,
                'user':user,
            }
        
        if formPartAddress.is_valid():
            formPart.save(commit=False)
            
            
           
            formPartAddress.save()
            
            return redirect("partnerLogged")
        else:
            print(formAddress.is_valid())
            print(formPartAddress.errors)
            
            formPart = PartnerInfoForm() 
            formPartAddress = PartnerAddressForm(request.POST,request.FILES,instance=user)
            context = {
                'formPart':formPart,
                'formPartAddress':formPartAddress,
                'user':user,
            }
            print(request.POST)
            return render(request,"partnerLogged/partnerLogged.html",context)    
        
    
       
    elif request.method == "POST" :
        if formPartAddress.is_valid():
            formPart.save(commit=False)
            
            
           
            formPartAddress.save()
            
            
        return redirect("partnerLogged")
    else:
        user = request.user.partner
        formPart = PartnerInfoForm(data,initial=data)   
        formPartAddress = PartnerAddressForm(data,initial=data2)
        context = {
                'formPart':formPart,
                'formPartAddress':formPartAddress,
                'user':user,
            }
        
        return render(request,"partnerLogged/partnerLogged.html",context) 
    
    
    
    
    
    
   