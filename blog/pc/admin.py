from django.contrib import admin
from requests import post
from .models import contact, login, post, signup

# Register your models here.
@admin.register(post)
class postModeladmin(admin.ModelAdmin):
 list_display=['id','title','desc']

@admin.register(signup)
class signupModeladmin(admin.ModelAdmin):
 list_display=['username','firstname','lastname','email','password']

@admin.register(login)
class loginModeladmin(admin.ModelAdmin):
 list_display=['username','password']

@admin.register(contact)
class contactModeladmin(admin.ModelAdmin):
 list_display=['name','email','phone','desc']