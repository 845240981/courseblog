# -*- coding: UTF-8 -*-
import xadmin
from .models import EmailVerifyRcord,Banner
from  xadmin import  views


class Basesetting(object):
    enable_themes =True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '慕学后台管理系统'
    site_footer = '脚脚'
    menu_style = 'accordion'


class EmailVerifyRcordAdmin(object):
    list_display =['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter =['code','email','send_type','send_time']


class BannerAdmin(object):


    list_display = ['title', 'image', 'url', 'add_time','index']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url', 'add_time','index']



xadmin.site.register(EmailVerifyRcord,EmailVerifyRcordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,Basesetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)