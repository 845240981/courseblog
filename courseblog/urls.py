from django.conf.urls import include, url
from django.contrib import admin
import xadmin
import django
from django.views.generic import  TemplateView
from django.views.static import serve
from  courseblog.settings import MEDIA_ROOT
from users.views import LoginView,RegisterView,AcitiveView,ForgetpwdView,PasswordresetView,ModifypwdView
urlpatterns = [
    # Examples:
    # url(r'^$', 'courseblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #django.conf.urls.url(r'^admin/', include(admin.site.urls)),
    url(r'^xadmin/',xadmin.site.urls),

    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^login$',LoginView.as_view(),name='login'),
    url(r'^register$',RegisterView.as_view(),name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'active/(?P<active_code>.*)/$',AcitiveView.as_view(),name='active'),
    url(r'forget/$',ForgetpwdView.as_view(),name='forget'),
    url(r'resetpwd/(?P<reset_code>.*)/$',PasswordresetView.as_view(),name='resetpwd'),
    url(r'modifypwd/$',ModifypwdView.as_view(),name='modifypwd'),


    url(r'^org/',include('organization.urls',namespace='org')),
    url(r'^media/(?P<path>.*)$' , serve, {'document_root':MEDIA_ROOT})



]
