from django.shortcuts import render , redirect 
from django.views.generic import View
from django.contrib.auth import authenticate , login , logout
from .forms import UserLoginForm , UserRegisterationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView , LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .mixins import LoginProtecter , LoginProtecterElse
from .models import User

class user_login(LoginProtecterElse,View):
    def post(self,request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'You logged successfully.')
                return redirect('company:home')
            else:
                messages.error(request,'Username or password is not correct.')
                return redirect('account:login')     
    def get(self,request):
        form = UserLoginForm()
        return render(request,'login.html',{'form':form})    


class user_logout(View,LoginProtecter):
    def get(self,request):
        logout(request)
        messages.success(request,'You logged out successfully.')
        return redirect("company:home")
         

class user_register(View):
    def post(self,request):
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'],password=cd['password'],bio=cd['bio'],profile_image=cd['profile_image'])
            user.save()
            user_name = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user2 = authenticate(username=user_name,password=password)
            login(request,user2)
            messages.success(request,"You registered and loggined successfully.")
            return redirect("company:home")

    def get(self,request):
        form = UserRegisterationForm()
        return render(request,'register.html',{'form':form})
