# -*- coding: UTF-8 -*-

from django.db import models
from users.models import Userprofile
from courses.models import Course
from datetime import  datetime

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'姓名')
    phone = models.CharField(max_length=20,verbose_name=u'电话号码')
    course_name = models.CharField(max_length=20, verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(Userprofile,verbose_name=u'用户')
    course = models.ForeignKey(Course,verbose_name=u'课程')
    content = models.CharField(max_length=200,verbose_name=u'评论内容')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural=verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(Userprofile,verbose_name=u'用户')
    fav_id = models.IntegerField(default=0,verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1,'课程'),(2,'授课机构'),(3,'讲师')),default=1,verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'课程收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user =models.IntegerField(default=0,verbose_name=u'用户id')
    message =models.CharField(max_length=300,verbose_name=u'信息内容')
    has_read = models.BooleanField(default=False,verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(Userprofile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name