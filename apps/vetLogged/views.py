from django.shortcuts import render, redirect
from .forms import VeteransSignUp2
from django.contrib.auth import authenticate, login
from django.contrib import messages

from apps.home.models import Veteran,Partner
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance 
import json
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.contrib.gis.serializers import geojson
# Create your views here.
def VetLogged(request):
    boolLoginBtn = 'btn-login' in request.POST
    boolSignupBtn = 'btn-signup' in request.POST
    print(boolLoginBtn)
    print(boolSignupBtn)
    user = request.user.veteran
    isSignedUp = user.vet_isSignedUp
    if request.method == 'POST' and boolLoginBtn:
        form1 = VeteransSignUp2(request.POST, request.FILES)
        
        print("SignUp Login Was PRESSED")
        if form1.is_valid():
            
            print(form1.is_valid())
            
           
            print(request.user)
            
            
            context = {
                'form1': form1,
                'isSignedUp' : isSignedUp,
                'user' : user,
                }
            
            return redirect('/vetLogged')
        else:
           
            context = {
                'form1': form1,
                'isSignedUp' : isSignedUp,
                'user' : user,
                }
            
            return redirect('/vetLogged')
            
   
    else:
        
        print("POST FROM ELSE")
        form1 = VeteransSignUp2()
        context = {
                'form1': form1,
                'isSignedUp' : isSignedUp,
                'user' : user,
                }
        
        
    return render(request,"vetLogged/map.html",context)
