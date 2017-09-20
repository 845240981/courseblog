# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.contrib.auth import  authenticate,login
# Create your views here.
from django.contrib.auth.backends import ModelBackend
from .models import Userprofile,EmailVerifyRcord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm,RegisterForm,ForgetForm,ModifyForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_email


class DefineBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = Userprofile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', )
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            pass

            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=user_name, password=password)
            if user is not None:
                if user.is_active:

                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '登陆失败'})

            else:
                return render(request, 'login.html', {'msg': '登陆失败'})
        else:
            return render(request, 'login.html', {'msg': '请确认自己账户密码zhengque'})



class AcitiveView(View):
    def get(self,request,active_code):
        all_record = EmailVerifyRcord.objects.filter(code=active_code)
        if all_record :
            for record in all_record:
                email = record.email
                user = Userprofile.objects.filter(email=email)[0]
                user.is_active =True
                user.save()
        else:
            return render(request,'active.html')
        return render(request,"login.html")

class ForgetpwdView(View):
    def get(self,request):
        forgetForm =ForgetForm()
        return render(request,'forgetpwd.html',{'Forgetform':forgetForm})
    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            user_name = request.POST.get('email','')
            asd=Userprofile.objects.filter(email=user_name)
            if Userprofile.objects.filter(email=user_name):
                 send_email(user_name,'forget')
                 return render(request,'send_success.html')
            else:
                return render(request, 'forgetpwd.html', {'msg': '该邮箱并没有注册'})
        return render(request, 'forgetpwd.html', {'Forgetform': forget_form})


class PasswordresetView(View):
    def get(self,request,reset_code):
        all_record = EmailVerifyRcord.objects.filter(code = reset_code)
        if all_record :
            for record in all_record:
                email = record.email
                return render(request,'password_reset.html',{'email':email})
        else:
            return render(request,'active.html')

class ModifypwdView(View):
    def post(self,request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            pwd1 =request.POST.get('password','')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email','')
            if pwd1 != pwd2:
                return render(request,'password_reset.html',{'email':email,'msg':'密码不一致'})
            user = Userprofile.objects.filter(email=email)[0]
            user.password = make_password(pwd2)
            user.save()
            return render(request,'login.html')
        else:
            email = request.POST.get('email','')
            return render(request,"password_reset.html",{'email':email,'modify_form':modify_form})

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email','')
            #if Userprofile.objects.filter(email=user_name):
                #return render(request, 'register.html', {'msg': '该邮箱已经被注册','register_form': register_form})
            password = request.POST.get('password','')
            userprofile = Userprofile()
            userprofile.username = user_name
            userprofile.email = user_name
            userprofile.password = make_password(password)
            userprofile.is_active =False
            userprofile.save()

            send_email(user_name, "register")
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})



def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        password = request.POST.get('password','')
        user =authenticate(username=user_name,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'index.html')
            else:
                return render(request,'login.html',{'msg':'用户违背'})
        else:
            return render(request,'login.html',{'msg':'登陆失败'})
    elif request.method == 'GET':
        return render(request,'login.html',)



