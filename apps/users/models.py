# -*- coding: UTF-8 -*-
from datetime import datetime
from xadmin import views
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Basesetting(object):
    enable_themes =True
    use_booswatch = True

class Userprofile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name=u'昵称')
    gender = models.CharField(choices=(('male',u'男'),('female',u'女')),default='female',max_length=8)
    address = models.CharField(max_length=100,default=u'')
    intrduction = models.CharField(max_length=100,default=u"",null=True,blank=True)
    mobile = models.CharField(max_length=10,null=True,blank=True,default=u'')
    Image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)



    class Meta:
        verbose_name =u'用户信息'
        verbose_name_plural =verbose_name


    #def __unicode__ (self):
       # return  self.username


class EmailVerifyRcord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email =models.EmailField(max_length=40,verbose_name=u'用户邮箱')
    send_type = models.CharField(choices=(('register',u'注册'),('forget',u'忘记密码')),max_length= 50,verbose_name=u'发送类型')
    send_time = models.DateField(default=datetime.now,verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name


   # def __unicode__(self):
        #return  '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(upload_to="banner/%Y/%m",verbose_name=u'轮播图',max_length=100)
    url = models.URLField(max_length=200,verbose_name=u"访问地址")
    index = models.ImageField(default='',verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name =u'轮播图'
        verbose_name_plural = verbose_name