# -*- coding: UTF-8 -*-

from .models import Course,Lesson,Video,Courseresource



import xadmin


class CourseAdmin(object):
    list_display =['name','degree','learn_time',]
    search_fields = ['name','degree','learn_time']
    list_filter =['name','degree','learn_time']


class LessonAdmin(object):
    list_display = ['course','add_time']
    search_fields = ['course']
    list_filter = ['course__name','add_time']


class CourseresourceAdmin(object):


    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):

    list_display = ['name','lesson','add_time']
    search_fields = ['name','lesson']
    list_filter = ['name','lesson','add_time']



xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(Courseresource,CourseresourceAdmin)