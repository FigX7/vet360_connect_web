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
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def getLocation(request):
    
    try:
        obj = request.user.veteran
    except:
        obj = request.user.partner
        
    try:
        obj = request.user.partner
    except:
        obj = request.user.veteran
    
    print("FROM getLOCation")
    print(obj)
    isSignedUp = False
    if request.is_ajax():
        print(isinstance(obj, Veteran))
        if isinstance(obj, Veteran):
            obj = Veteran.objects.get(pk=request.user.veteran.user_id)
            isSignedUp = obj.vet_isSignedUp
            if request.method == "POST":
                # no need to do this
                print("FROM AJAX")
                toDict = request.POST.get('getdata')  
                coords = json.loads(toDict)
                
                
                obj.vet_Lat = coords['lat']
                obj.vet_Lon = coords['lon' ]
                point = Point(coords['lat'],coords['lon' ])
                obj.vet_point = point
                
                obj.save()
            elif request.method == "GET":
                point = obj.vet_point
                geoQuery = "test get data"
                try:
                    geoQueryVets = Veteran.objects.filter(vet_point__distance_lt=(point, Distance(km=50))).defer('vet_point').values('vet_Lat','vet_Lon','vet_branch','username','ava_user').exclude(username = request)
                    geoQueryPartners = Partner.objects.filter(partner_point__distance_lt=(point, Distance(km=50))).defer('partner_point').values('partner_Lat','partner_Lon','username','ava_user').exclude(username = request)
                except:
                    print(ERRORS)
                print(geoQueryPartners)
                listVetsPoints = {}
                listPartnersPoints = {}
                i = 0;
                i2 = 0;
                for x in geoQueryVets:
                    i = i+1
                    listVetsPoints[i] = x
                for y in geoQueryPartners:
                    i2 = i2+1
                    listPartnersPoints[i2] = y
                #jsonGeo = json.dumps()listVets)
                context = {
                        "queryVet": listVetsPoints,
                        "queryPartners": listPartnersPoints,
                        
                }
                    
                return JsonResponse(context)
        if isinstance(obj, Partner):
            obj = Partner.objects.get(pk=request.user.partner.user_id)
            isSignedUp = False
            if request.method == "POST":
                # no need to do this
                print("FROM AJAX")
                toDict = request.POST.get('getdata')  
                coords = json.loads(toDict)
                
                
                obj.partner_Lat = coords['lat']
                obj.partner_Lon = coords['lon' ]
                point = Point(coords['lat'],coords['lon' ])
                obj.partner_point = point
                
                obj.save()
            elif request.method == "GET":
                point = obj.partner_point
                geoQuery = "test get data"
                try:
                    geoQueryVets = Veteran.objects.filter(vet_point__distance_lt=(point, Distance(km=50))).defer('vet_point').values('vet_Lat','vet_Lon','vet_branch','username','ava_user').exclude(username = request)
                    geoQueryPartners = Partner.objects.filter(partner_point__distance_lt=(point, Distance(km=50))).defer('partner_point').values('partner_Lat','partner_Lon','username').exclude(username = request)
                except:
                    print(ERRORS)
                print(geoQueryPartners)
                listVetsPoints = {}
                listPartnersPoints = {}
                i = 0;
                for x in geoQueryVets:
                    i = i+1
                    listVetsPoints[i] = x
                for y in geoQueryPartners:
                    i = i+1
                    listPartnersPoints[i] = x 
                #jsonGeo = json.dumps()listVets)
                context = {
                        "queryVet": listVetsPoints,
                        "queryPartners": listPartnersPoints,
                        
                }
                    
                return JsonResponse(context)    
    # make sure that you serialise "request_getdata" 
    context = {

    'isSignedUp' : isSignedUp,  
    'user' : obj,
}
    
        # make sure that you serialise "request_getdata" 
    
    return HttpResponse(context)#     user = request.user.veteran
#     vet_Lat = user.vet_Lat
#     vet_Lon = user.vet_Lon
#     data ={'vet_Lat':vet_Lat,
#            'vet_Lon':vet_Lon,}
    