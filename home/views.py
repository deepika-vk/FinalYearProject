from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from accounts.models import profile
from django.core.mail import send_mail
import uuid
def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')
def log_in(request):
    if request.user.is_authenticated:
            return render(request,'404.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            context={'greenalert':"login successful"}
            return render(request,'home.html',context)
        if User.objects.filter(username=username).exists():
            context={'redalert':"wrong password"}
            return render(request,'login.html',context)
        context={'redalert':"User name doesn't exist"}
        return render(request,'login.html',context)
    else:
        return render(request,'login.html')
def log_out(request):
     if request.user.is_authenticated:
        logout(request)
        context={'greenalert':"logout successful"}
        return render(request,'home.html',context)
     return render(request,'404.html')    
def register_page(request):
    if request.user.is_authenticated:
            return render(request,'404.html')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        if " " in username or "@" in username:
            context={'redalert':'username should not contain spaces and @'}
            return render(request,'register.html',context)
        user_obj = profile.objects.filter(email = email)
        if User.objects.filter(username=username).exists() or profile.objects.filter(user=username).exists():
            context={'redalert':'username already taken'}
            return render(request,'register.html',context)
        if user_obj.exists() :
            user_obj=user_obj[0]
            if user_obj.email_verified==True:
                context={'redalert':'email already taken'}
                return render(request,'register.html',context)
            else:
                user_obj.user=username
                user_obj.first_name = first_name
                user_obj.last_name= last_name
                user_obj.save()
                
        else:
            profile.objects.create(first_name = first_name , last_name= last_name , email = email , user =username)
        try:
            send_verification_mail(request,email)
            context={'greenalert':'verification email sent'}
            return render(request,'register.html',context)
        except Exception as e:
            context={'redalert':'Something went wrong, try again'}
            return render(request,'register.html',context)
    return render(request,'register.html')   