from django.shortcuts import render,redirect
from django.contrib import auth
from apps.home.models import Veteran, User, Partner
# Create your views here.
def LogoutCustom(request):
    user = request.user
    print(user.isPart)
    print (user.isVet)
    if user.isPart:
       user.partner.partner_Lat = 0.0
       user.partner.partner_Lon = 0.0
       user.partner.save()
    elif user.isVet:
        user.veteran.vet_Lat = 0.0
        user.veteran.vet_Lon = 0.0
        user.veteran.save()
    
    auth.logout(request)
    return redirect("home")