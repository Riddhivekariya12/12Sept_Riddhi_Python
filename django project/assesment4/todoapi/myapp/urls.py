from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('task_list/<int:id>',views.task_list),
    path('task_details/<int:id>',views.task_details),
]