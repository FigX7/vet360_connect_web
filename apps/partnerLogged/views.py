
from .forms import PartnerInfoForm
# Create your views here.
from django.shortcuts import render, redirect
from apps.home.models import Partner
def PartnerLogged(request):
    boolPartInfo = 'btn-PartInfo' in request.POST
    
    boolPartGeoCode ='btn-geocode' in request.POST
    print(boolPartInfo)
    
    print(boolPartGeoCode)
    user = request.user.partner
    data = {
        'partner_web_address':user.partner_web_address,
        'partner_state':user.partner_state,
        'partner_zip':user.partner_zip,
        'partner_phone':user.partner_phone,
        'partner_name':user.partner_name,
        'partner_address1':user.partner_address1,
        'partner_address2':user.partner_address2,
        'partner_mission':user.partner_mission,
        
    }
   
    if request.method == 'POST':
        print(request.POST)
        user = request.user.partner
        formPart = PartnerInfoForm(request.POST,request.FILES,instance=user)
        
        context = {
                'formPart':formPart,
                'user':user,
            }
        
        if formPart.is_valid():
            formPart.save(commit=False)
            
            
            
            user.ava_user = user.partner_logo
            user.save()
           
            formPart.save()
            
            
            return redirect("partnerLogged")
        else:
            print(formPart.is_valid())
            print(formPart.errors)
            
            formPart = PartnerInfoForm(request.POST,request.FILES,instance=user) 
            
            context = {
                'formPart':formPart,
                'user':user,
            }
            print(request.POST)
            return render(request,"partnerLogged/partnerLogged.html",context) 
    
    else:
        user = request.user.partner
        formPart = PartnerInfoForm(data,initial=data)
        context = {
                'formPart':formPart,
                'user':user,
            }
        
        return render(request,"partnerLogged/partnerLogged.html",context) 
    
    
    
    
    
    
   