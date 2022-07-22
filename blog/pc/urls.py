from django import views
from django.contrib import admin
from django.urls import path
from pc import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.index,name='pc'),
    path("about",views.about,name='about'),
    path("contact",views.Contact,name='contact'),
    path("login",views.user_login,name='login'),
    path("signup",views.signin,name='signup'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("logout",views.user_logout,name='logout'),
    path("addpost",views.add_post,name='addpost'),
    path("updatepost/<int:id>",views.update_post,name='updatepost'),
    path("deletepost/<int:id>",views.delete_post,name='deletepost')
   
]
