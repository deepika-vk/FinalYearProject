from django.contrib import admin
from django.urls import path,include
from settings import views
urlpatterns = [
    path('',views.settings),
    path('leetcode_name/',views.leetcode_name),
    path('leetcode_check/',views.leetcode_check),
    path('codechef_name/',views.codechef_name),
    path('codechef_check/',views.codechef_check),
    path('codeforces_name/',views.codeforces_name),
    path('codeforces_check/',views.codeforces_check),
    path('institute/',views.change_institute),    
    
]