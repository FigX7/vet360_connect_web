
from django.shortcuts import render, redirect
from apps.home.models import Veteran,Partner,User
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance 
import json
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.contrib.gis.serializers import geojson
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# Create your views here.

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
                    if obj.vet_isSignedUp == True:
                        geoQueryVets = Veteran.objects.filter(vet_point__distance_lt=(point, Distance(km=50))).defer('vet_point').values('vet_Lat','vet_Lon','vet_branch','username','ava_user')
                        geoQueryPartners = Partner.objects.filter(partner_point__distance_lt=(point, Distance(km=50))).defer('partner_point').values('partner_Lat','partner_Lon','username','ava_user')
                    else:
                        geoQueryPartners = Partner.objects.filter(partner_point__distance_lt=(point, Distance(km=50))).defer('partner_point').values('partner_Lat','partner_Lon','username','ava_user')
                        geoQueryVets  = {}
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
                    geoQueryVets = Veteran.objects.filter(vet_point__distance_lt=(point, Distance(km=50))).defer('vet_point').values('vet_Lat','vet_Lon','vet_branch','username','ava_user')
                    geoQueryPartners = Partner.objects.filter(partner_point__distance_lt=(point, Distance(km=50))).defer('partner_point').values('partner_Lat','partner_Lon','username')
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
@csrf_exempt
def getGeocode(request):
    try:
        partObj = request.user.partner
    except:
        print("errro in Ajax GOeocode try")
    if request.is_ajax():
        if request.method == "POST":
            toDictGeocode = request.POST.get('getdata') 
            geoCoords = json.loads(toDictGeocode)
            partObj.partner_Lat = geoCoords[0]["geometry"]["location"]["lat"]
            partObj.partner_Lon = geoCoords[0]["geometry"]["location"]["lng"]
            geoDict = {'geoCoords':geoCoords}
            return JsonResponse(geoDict)
        else:
            obj = 'TEST'
            context = {
                    'obj' : obj,
                }
            return JsonResponse(context) 
        
        
        
@csrf_exempt
def setPartnerPos(request):
    
    obj = request.user.partner
    part_Pos= request.POST.get("getdata")
    partCoords = json.loads(part_Pos)
    obj.partner_Lat = partCoords['lat']
    obj.partner_Lon = partCoords['lng']
    obj.save()
    context = {'part_Pos':part_Pos}
    return JsonResponse(context) 
    if request.is_ajax():
        obj = 'TEST'
        context = {
            'obj' : obj,
            }
    return JsonResponse(context) 
    
        