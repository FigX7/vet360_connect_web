from django.contrib.gis.db import models
from localflavor.us.us_states import STATE_CHOICES
# Create your models here.

from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.fields import FloatField

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


    


# Create your models here.

class User(AbstractUser):
    objects = CustomUserManager()
    ava_user = models.ImageField(upload_to ='avatars',blank = True, null =True, default="avatars/default.png")
    isPart = models.BooleanField(default = False)
    isVet = models.BooleanField(default = False)
    def __str__(self):
        return str(self.username)
    
        
class Veteran(User):
    VET_BRANCH_CHOICES = (
    ('','---------'),
    ('usaf','Air Force'),
    ('usa', 'Army'),
    ('uscg', 'Coast Guard'),
    ('usmc', 'Marines'),
    ('usn', 'Navy'),

    
    )
    VET_BOOL_CHOICES = (
    ('','---------'),
    (True,'Yes'),
    (False, 'No'),

    
    )

    user = OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
   
    ###--------------------------------- Personal Info ---------------------###
   
    vet_mobile = models.CharField(max_length = 12,blank = True, null =True)
    vet_state  = models.CharField(max_length =2,choices=STATE_CHOICES,verbose_name="state",blank = True, null =True)
    vet_zip = models.CharField(max_length = 5 , blank = True, null =True)
    ###--------------------------------- Combat Info ---------------------###
    vet_branch = models.CharField(max_length = 4,choices=VET_BRANCH_CHOICES,verbose_name="vet_branch")
    vet_unit = models.CharField(max_length = 50,blank = True, null =True)
    vet_isPost911 = models.BooleanField(blank = True, null =True,choices=VET_BOOL_CHOICES,verbose_name="vet_isPost911")
    vet_isCombat = models.BooleanField(blank = True, null =True,choices=VET_BOOL_CHOICES,verbose_name="vet_isCombat")
    
    ###--------------------------------- Misc. INfo for web app ---------------------###
    vet_isVet = models.BooleanField(default = True)
    vet_isNotifications =  models.BooleanField(blank = True, null =True,choices=VET_BOOL_CHOICES,verbose_name="vet_isNotifications")
    vet_isShared =  models.BooleanField(blank = True, null =True,choices=VET_BOOL_CHOICES,verbose_name="vet_isShared")
    vet_isSignedUp  =  models.BooleanField(blank = True, null =True,choices=VET_BOOL_CHOICES,verbose_name="vet_isSignedUp")
    vet_Lat = models.FloatField(blank = True, null =True,default=0.0)
    vet_Lon = models.FloatField(blank = True, null =True,default=0.0)
    vet_point = models.PointField(null=True, blank=True,default ="0101000020E6100000EC884336906740407B911A248E495DC0" )
    class Meta:
        
        db_table = 'veteran'  
    def __str__(self):
        return str(self.user)
class Partner(User):
     ###--------------------------------- Company Info ---------------------###
    user = OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    
    partner_phone = models.CharField(max_length = 12,blank = True, null =True)
    partner_address1 = models.CharField(max_length = 300, blank = True,null = True)
    partner_address2 = models.CharField(max_length = 300, blank = True,null = True)
    partner_state  = models.CharField(max_length =2,choices=STATE_CHOICES,verbose_name="state",blank = True, null =True)
    partner_zip = models.CharField(max_length = 5 , blank = True, null =True)
    partner_name = models.CharField(max_length = 300, blank = True,null = True)
   
    partner_mission = models.CharField(max_length = 300, blank = True,null = True)
    partner_logo = models.ImageField(upload_to ='partnerLogos',blank  = True,null = True,default="avatars/default.png")
    
     ###--------------------------------- Misc. INfo for web app ---------------------###
    partner_web_address = models.CharField(max_length = 255,blank = True, null = True)
    partner_isPart = models.FloatField(default = True);
    partner_Lat = models.FloatField(blank = True, null =True,default=0.0)
    partner_Lon = models.FloatField(blank = True, null =True,default=0.0)
    partner_point = models.PointField(null=True, blank=True,default ="0101000020E6100000EC884336906740407B911A248E495DC0" )
    
    
    class Meta:
        
        db_table = 'partner'  
    def __str__(self):
        return str(self.user)
    
