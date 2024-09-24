from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
        path('',views.home),
     path('about/',views.about),
        path('login/',views.log_in),
    path('logout/',views.log_out),
      path('register/',views.register_page),
]