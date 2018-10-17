from django.contrib import admin
from .models import User,Veteran,Partner
# Register your models here.
admin.site.register(User)
admin.site.register(Veteran)
admin.site.register(Partner)