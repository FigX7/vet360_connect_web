from django.shortcuts import render


# Create your views here.
def VaultPage(request):
    return render(request,"vault/vault.html")