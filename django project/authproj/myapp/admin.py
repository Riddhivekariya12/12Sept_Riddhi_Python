from django.contrib import admin

# Register your models here.

from django.urls import path
from myapp import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_views.contact_view, name='contact'),
]