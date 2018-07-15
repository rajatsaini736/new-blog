"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'account/login/$',auth_views.login,name='login'),
    url(r'account/logout/$',auth_views.logout,name='logout'),
    url(r'accounts/logout/$',auth_views.logout,name='logout',kwargs={'next_page':'/'}),
    url(r'signup/$',views.SignUp.as_view(),name='signup')
]
