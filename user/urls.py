from django.contrib import admin
from django.urls import path, include
from .views import signup,LoginView,logout,index,contact,group,createcontact,creategroup,send_mail_to_mul

urlpatterns = [
    path('signup/',signup,name="signup"),
    path('signin/',LoginView.as_view(),name="signin"),
    path('allcontacts/',contact,name="allcontacts"),
    path('createcontacts/',createcontact,name="createcontacts"),
    path('creategroups/',creategroup,name="creategroup"),
    path('allgroups/',group,name="allgroups"),
    path('logout/',logout,name="logout"),
    path('send_mail', send_mail_to_mul, name='sendemail'),
    path('',index,name="index")
    

]