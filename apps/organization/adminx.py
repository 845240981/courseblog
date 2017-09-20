
import xadmin


from django.contrib import admin

# Register your models here.

from .models import CityDict,CourseOrg,Teacher

class CitysAdmin(object):

    list_display = ['des', 'name','add_time']
    search_fields = ['des', 'name']
    list_filter = ['des', 'name','add_time']



class TeacherAdmin(object):

    list_display = ['org', 'name','work_years']
    search_fields = ['org', 'name','work_years']
    list_filter = ['org', 'name','work_years']


class CourseorgAdmin(object):
    list_display = ['name', 'click_nums','city']
    search_fields =  ['name', 'click_nums','city']
    list_filter =  ['name', 'click_nums','city']








xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CityDict,CitysAdmin)
xadmin.site.register(CourseOrg,CourseorgAdmin)