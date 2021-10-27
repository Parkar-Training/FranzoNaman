"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import admin as admin
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from user.views import User # emailOtp, OTP2
from user.logIn import login
from user.deleteUser import deleteUser
from user.verifyOtp import verifyOtp
from user.SendPutOtp import emailOtp
#from user.views import LogIn#User
#UserList, UserDetail, User
#from user.views import showData
from user.GetPutPublic import getPublic
from user.searchUser import searchUser

urlpatterns = [
    path('admin/', admin.site.urls),
   # url(r'^api/show/(?P<userId>\d+)/$', UserDetail.as_view(),name='user_list'),


  #  path('view/', showData(),name='show data')


   # url(r'^api/show/$', UserList.as_view(), name='user_list'),

    url(r'^api/signup$',view=User),
    url(r'^api/put$',view=User),
    url(r'^api/emailOtp2$',view=emailOtp),

    url(r'^api/otp/(?P<userId>\d+)/$',emailOtp.as_view(),name = 'otp store'),
   # url(r'^api/otp$',view=OTP2.as_view()),
  #  url(r'^api/emailOtp$',emailOtp.as_view()),
    url(r'^api/delete/(?P<userId>\d+)/$',deleteUser.as_view(),name='delete user'),

    url(r'^api/login$', login.as_view()),


    url(r'^api/verify$', verifyOtp.as_view()),
    #url(r'^api/login$',view= LogIn)
    url(r'^api/showPublic$', getPublic.as_view()), # show only public url
    url(r'^api/putPublic/(?P<userId>\d+)/$', getPublic.as_view(),name='put user private mode'), #changes private or public

    url(r'^api/searchUser$',searchUser.as_view(),name='search_User')

]
