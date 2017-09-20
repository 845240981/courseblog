# -*- coding: UTF-8 -*-

from django.db import models
from datetime import datetime
# Create your models here.



class CityDict(models.Model):
    name =models.CharField(max_length=50,verbose_name=u'名字')
    des = models.CharField(max_length=300,verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural =verbose_name

    def __unicode__(self):
        return self.name



class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'机构名称')
    dec = models.TextField(verbose_name=u'机构简介')
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数量')
    catogory = models.CharField(verbose_name=u'机构类别',max_length=60,default='pxjg',choices=(('pxjg','培训机构'),('gr','个人'),('gx','高校')))
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏数')
    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u'封面图')
    address = models.CharField(max_length=150,verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    students = models.IntegerField(default=0,verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0,verbose_name=u'课程数量')


    class Meta:
        verbose_name = u'授课机构'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数量')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u'教师图片')
    work_company = models.CharField(max_length=150, verbose_name=u'机构地址')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')

    class Meta:
        verbose_name = u'教师简介'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
