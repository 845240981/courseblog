# -*- coding: UTF-8 -*-

from .models import UserAsk,UserCourse,UserMessage,UserFavorite,CourseComments



import xadmin


class UserAskAdmin(object):
    list_display =['name','phone','course_name',]
    search_fields = ['name','phone','course_name']
    list_filter =['name','phone','course_name']


class UserCourseAdmin(object):
    list_display = ['user','course']
    search_fields = ['user','course']
    list_filter = ['user','course']


class CourseCommentsAdmin(object):


    list_display = ['user','course','content']
    search_fields = ['user','course','content']
    list_filter = ['user','course','content']

class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id','fav_type','add_time']
    search_fields = ['user', 'fav_id','fav_type']
    list_filter = ['user', 'fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read']


xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)