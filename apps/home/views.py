from django.shortcuts import render, redirect
#from django.core import serializers
from django.contrib.auth import login, authenticate
from apps.home.forms import VeteranSignUpForm, VetLoginForm, PartnerSignUpForm, PartnerLoginForm
from .models import User,Partner,Veteran
from django.contrib import messages
from social_core.utils import user_is_authenticated



# Create your views here.

def Home(request):
    
    boolLoginBtn = 'btn-login' in request.POST
    boolSignupBtn = 'btn-signup' in request.POST
    boolPartLoginBtn = 'partbtn-login' in request.POST
    boolPartSignupBtn = 'partbtn-signup' in request.POST
    print(boolLoginBtn)
    print(boolSignupBtn)
    print(boolPartLoginBtn)
    print(boolPartSignupBtn)
    if request.method == 'POST' and boolLoginBtn:
        baseHtml = "home/index.html"
        form2 = VeteranSignUpForm()
        form1 = VetLoginForm(request.POST, request.FILES)
        form4 = PartnerSignUpForm()
        form3 = PartnerLoginForm()
        print("SignUp Login Was PRESSED")
        if form1.is_valid():
            
            print(form1.is_valid())
            
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password')
            
            user = authenticate(username=username, password=raw_password)
            
            print(user)
            
            if user == None:
                messages.error(request, "Login Credientials incorrect")
            else:
                login(request, user)
            print("TEST" + str(request.user.is_authenticated))
            context = {
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                
                }
            
            if request.user.is_authenticated:
                return redirect('/vetLogged')
                
                print(baseHtml)
                
            return render(request,baseHtml,context)
        else:
           
            print(request.POST)
            print(form1.errors)
            context = {
                
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                }
            print(baseHtml)
            return render(request,baseHtml,context)

            
    elif request.method == 'POST' and boolSignupBtn :
        baseHtml = "home/index.html"
        form2 = VeteranSignUpForm(request.POST, request.FILES)
        form1 = VetLoginForm()
        form4 = PartnerSignUpForm()
        form3 = PartnerLoginForm()
    
        if form2.is_valid():
            print(form2.is_valid())
                  
            username = form2.cleaned_data.get('username')
            
            
            raw_password = form2.cleaned_data.get('password1')
            
            user = form2.save()
            user.isVet = True
            user = form2.save()
            login(request, user)
            print("TEST" + str(request.user.is_authenticated))
            context = {
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                
                }
            
            if request.user.is_authenticated:
                return redirect('/vetLogged')
                
                print(baseHtml)
                
            return render(request,baseHtml,context)
        else:
            print(form2.errors)
            context = {
                
                'form1': form1,
                'form2': form2,
                }
            print(request.POST)
            return render(request,baseHtml,context)
    elif request.method == 'POST' and boolPartLoginBtn:
        baseHtml = "home/index.html"
        form2 = VeteranSignUpForm()
        form1 = VetLoginForm()
        form4 = PartnerSignUpForm()
        form3 = PartnerLoginForm(request.POST, request.FILES)
        print("SignUp Login Was PRESSED")
        if form3.is_valid():
            
            print(form3.is_valid())
            
            username = form3.cleaned_data.get('username')
            raw_password = form3.cleaned_data.get('password')
            
            user = authenticate(username=username, password=raw_password)
            print(user)
            
            if user == None:
                messages.error(request, "Login Credientials incorrect")
            else:
                login(request, user)
            print("TEST" + str(request.user.is_authenticated))
            context = {
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                
                }
            
            if request.user.is_authenticated:
                return redirect('/partnerLogged')
                
                print(baseHtml)
                
            return render(request,baseHtml,context)
        else:
           
            print(request.POST)
            print(form3.errors)
            context = {
                
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                }
            print(baseHtml)
            return render(request,baseHtml,context)

            
    elif request.method == 'POST' and boolPartSignupBtn :
        baseHtml = "home/index.html"
        form2 = VeteranSignUpForm(request.POST, request.FILES)
        form1 = VetLoginForm()
        form4 = PartnerSignUpForm(request.POST, request.FILES)
        form3 = PartnerLoginForm()
        
    
        if form4.is_valid():
            print(form4.is_valid())
                  
            username = form4.cleaned_data.get('username')
            
            
            raw_password = form4.cleaned_data.get('password1')
            
            user = form4.save()
            
            
            login(request, user)
            print("TEST" + str(request.user.is_authenticated))
            context = {
               
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                
                }
            
            if request.user.is_authenticated:
                return redirect('/partnerLogged')
                
                print(baseHtml)
                
            return render(request,baseHtml,context)
        else:
            print(form4.errors)
            context = {
                
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                }
            print(request.POST)
            return render(request,baseHtml,context)
                   
    else:
        
        print("POST FROM ELSE")
        form2 = VeteranSignUpForm()
        form1 = VetLoginForm()
        form4 = PartnerSignUpForm()
        form3 = PartnerLoginForm()
        context = {
                'form1': form1,
                'form2': form2,
                'form1': form1,
                'form2': form2,
                'form4': form4,
                'form3': form3,
                }
        baseHtml = "home/index.html"
        
        print(request.user)
        homeUrl = "/vetLogged"
       
        if request.user.is_authenticated:
            print(request.user.isPart)
            print(request.user.isVet)
            if request.user.isPart:
                homeUrl = "/partnerLogged"
                return redirect(homeUrl)
            elif request.user.isVet:
        
                homeUrl = "/vetLogged"
                return redirect(homeUrl)
    
        print(baseHtml)
    return render(request,baseHtml,context)