from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('signin/',views.signin,name='signin'),
   path('signup/',views.signup),
   path('notes/',views.notes,name='notes'),
   path('profile/',views.profile),
   path('about/',views.about),
   path('contact/',views.contact),
   path('otpverify/',views.otpverify,name='otpverify'),
   path('userlogout/',views.userlogout),
]