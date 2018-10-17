from django.shortcuts import render


# Create your views here.
def VaultVolunteer(request):
    return render(request,"vault_volunteer/vault_volunteer.html")