from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def PartnerLogged(request):
   return render(request,"partnerLogged/partnerLogged.html")