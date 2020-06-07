from django.contrib import admin
from django.urls import path, include
from .views import signup,LoginView,logout,index

urlpatterns = [
    path('',signup,name="signup"),
    path('signin/',LoginView.as_view(),name="signin"),
    path('logout/',logout,name="logout"),
    path('home/',index,name="index")
    

]