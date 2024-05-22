from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',views.task_list),
    path('tasks/<int:pk>',views.task_detail),
    
]
