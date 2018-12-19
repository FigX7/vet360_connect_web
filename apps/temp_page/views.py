from django.shortcuts import render


# Create your views here.
def TempPage(request):
    return render(request,"tempPage/index.html")