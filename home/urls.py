from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.home),
    path('login/',views.log_in),
    path('logout/',views.log_out),
    path('register/',views.register_page),
    path('password/<token>',views.set_password),
    path('forget_password/',views.forget_password),
    path('forget_username/',views.forget_username),
     path('about/',views.about),
]