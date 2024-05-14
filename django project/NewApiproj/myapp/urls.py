from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('getstid/<int:id>',views.getstid),
    path('deletestid/<int:id>',views.deletestid),
    path('savestdata/<int:id>',views.savestdata),
    path('updatestdata/<int:id>',views.updatestdata),
]