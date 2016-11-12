"""lvmeng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,handler404,handler500
from django.contrib import admin
from django.conf.urls.static import static
from lvmeng import settings
from django.views.generic.base import RedirectView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
from erp import views2
import web_customer.views
from erp.tests import test_login

handler404 = "erp.views.page_not_found"
handler500 = "erp.views.page_error"


urlpatterns = [
    #admin
    url(r'admin/', include(admin.site.urls)),

    #homepage
    url(r'^$', web_customer.views.homePage),
    url(r'^ie8', web_customer.views.homePage_ie8),
    url(r'^mobi/$', web_customer.views.mobile_homePage),

    #login
    url(r'customer_login/$', web_customer.views.customer_login),
    url(r'login/$', views2.account_login),

    url(r'test/$', test_login),#test for login

    #inner app
    url(r'^api/', include('api.urls')),
    url(r'^agent_api/', include('agent_api.urls')),
    url(r'^message_api/', include('message_api.urls')),
    url(r'^push/', include('push.urls')),
    url(r'^erp/', include('erp.urls')),
    url(r'^oa/', include('oa.urls')),
    url(r'^web_customer/', include('web_customer.urls')),
    url(r'^mobi/', include('mobi.urls')),
    url(r'^invest/', include('investment.urls')),

    #outer app
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),#TODO:need to remove csrf_exempt in production
    # url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^captcha/', include('captcha.urls')),

    #account
    # url(r'^password_change/', 'django.contrib.auth.views.password_change', {'post_change_redirect': '/password_change_done/'}),
    url(r'^password_change/', 'django.contrib.auth.views.password_change', {'post_change_redirect': '/'}),
    url(r'^password_change_done/', 'django.contrib.auth.views.password_change_done'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # url(r'admin/', include(admin.site.urls)),
    # url(r'^$', include('web_customer.urls')),
    # url(r'^web_customer/', include('web_customer.urls')),
    # url(r'^mobi/$', web_customer.views.mobile_homePage),
    # url(r'^announcement/$', web_customer.views.announcement),
    # url(r'^tinymce/',include('tinymce.urls')),
]

#todo has to be removed in production
#this will serve media files during development environment, otherwise files uploaded by users won't be recognized
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
