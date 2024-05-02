from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
   path('',views.index),
   path('otpverification/',views.otpverification),
   path('signin/',views.signin),
   path('signup/',views.signup),
]  