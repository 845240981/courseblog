
from django import forms
from captcha.fields import  CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class ModifyForm(forms.Form):
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
