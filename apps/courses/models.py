# -*- coding: UTF-8 -*-

from django.db import models

from datetime import  datetime
from organization.models import  CourseOrg
# Create your models here.

class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name=u'所属机构',null=True,blank=True)
    name = models.CharField(max_length=20,verbose_name=u'课程名')
    des = models.CharField(max_length=100,verbose_name=u'课程简介')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')),max_length=20)
    learn_time = models.IntegerField(default=0,verbose_name=u'学习时长')
    learn_nums = models.IntegerField(default=0,verbose_name=u'学习人数')
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数量')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏人数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name= u'添加时间')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面')


    class Meta:
        verbose_name =u'课程'
        verbose_name_plural=verbose_name


    def __unicode__(self):
        return self.name



class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=100,verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')


    class Meta:
        verbose_name =u'章节'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u'章节')
    name = models.CharField(max_length=20,verbose_name=u'视频名')
    add_time = add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name



class Courseresource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=50,verbose_name=u'名称')
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u'下载')
    add_time = add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name




