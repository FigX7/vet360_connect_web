"""vet360_connect_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.vetLogged import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'',include('apps.home.urls')),
    url(r'vetLogged', include('apps.vetLogged.urls')),
    url(r'partnerLogged', include('apps.partnerLogged.urls')),
    url(r'vault', include('apps.vault.urls')),
    url(r'vault_volunteer', include('apps.vaultVolunteer.urls')),
    url(r'vetProfile', include('apps.vetProfile.urls')),
    url(r'^ajax/getLocation/$', views.getLocation, name='getLocation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
