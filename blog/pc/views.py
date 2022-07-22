import datetime
from pdb import post_mortem
from turtle import update
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate
from pc.admin import postModeladmin
from pc.models import contact, login, post, signup



def index(request):
      posts=post.objects.all()
      
      return render(request,"index.html",{'posts':posts})

def about(request):
      return render(request,"about.html")

def Contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        request.session["name"]=name
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        Contact = contact(name=name,email=email,phone=phone,desc=desc)
        Contact.save()
        messages.success(request, 'Your message has been sent!')
        if 'loggin' in request.session:
            return render(request,"contact.html",{'login':request.session['loggin'],'name':request.session['name']})
        else:
            return render(request,"contact.html",{'login':False,'name':request.session['name']})
    else:
        if 'loggin' in request.session:
            return render(request,"contact.html",{'login':request.session['loggin'],'name':request.session['name']})
        else:
            return render(request,"contact.html",{'login':False,'name':'UNKNOWN'})
        

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        if authenticate(request,username=username,password=password):
            user1=authenticate(request,username=username,password=password)
            login(request,user1)
            
            request.session['login']=True
            request.session['adminloggin']=True
            request.session['name']=username
            posts=post.objects.all()
            return render(request,'dashboard.html',{'posts':posts,'login':request.session['login'],'name':request.session['name'],'admin':request.session['adminloggin']}) 
          

        elif signup.objects.filter(username=username,password=password).count()>0:
            login.objects.update_or_create(username=username)
            messages.success(request,username+' has successfully logged in')
            request.session['login']=True
            request.session['adminloggin']=False
            request.session['name']=username
            posts=post.objects.all()  
            return render(request,'dashboard.html',{'posts':posts,'login':request.session['login'],'name':request.session['name'],'admin':request.session['adminloggin']}) 
            
        else:
            
            print (signup.objects.filter(username=username,password=password).count()>0)
            return render(request,'login.html') 
    else:
        return render(request,'login.html') 

     

def signin(request):
   if request.method=="POST":
        username=request.POST.get('username') 
        firstname=request.POST.get('firstname') 
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        signup.objects.create(username=username,firstname=firstname,lastname=lastname,email=email,password=password)
        messages.success(request,username+ " you have successfully created a acount")
        return render(request,'login.html')
   else:
        return render(request,'signup.html')
     

def dashboard(request):
   if request.session['loggin']:
      posts=post.objects.all()
      return render(request,"dashboard.html",{'posts':posts})
   else:
        return HttpResponse('/login')

def user_logout(request):
    
    print(request.session.values())
    if 'username' in request.session:
        del request.session['name']
        del request.session['login']
        messages.error(request,'you have been successfully logged out!!!')
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def add_post(request):
    if request.method=='POST':
        title=request.POST.get("title")
        desc = request.POST.get("desc")
        add_post = post(title=title,desc=desc)
        add_post.save()
        posts=post.objects.all()
        messages.success(request,'You have successfully Add the post,Thank you!')
        return render(request,'dashboard.html',{'posts':posts})
    else:
        if 'login' in request.session:
            return render(request,"addpost.html",{'login':request.session['login'],'name':request.session['name']})
        else:
            return render(request,"index.html",{'login':False,'name':request.session['name']})


def update_post(request,id):
    if request.method=='POST':
        pi=post.objects.filter(pk=id)
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        pi.update(title=title,desc=desc)
        posts=post.objects.all()
        messages.success(request,'You have successfully updated the post,Thank you!')
        return render(request,'dashboard.html',{'posts':posts})
    else:
        if 'login' in request.session:
            pi=post.objects.get(pk=id)
            return render(request,"updatepost.html",{'login':request.session['login'],'name':request.session['name'],'post':pi})
        else:
            return render(request,"index.html",{'login':False,'name':request.session['name']})

def delete_post(request,id):
    
     if request.method=='POST':
        pi=post.objects.get(pk=id)
        pi.delete()
        posts=post.objects.all()
        messages.success(request,'You have successfully deleted the post,Thank you!')
        return render(request,'dashboard.html',{'posts':posts})
     if 'login' in request.session:
            return render(request,"dashboard.html",{'login':request.session['login'],'name':request.session['name']})
     else:
            return render(request,"index.html",{'login':False,'name':request.session['name']})

# Create your views here.
