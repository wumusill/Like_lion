from django.contrib import admin
from django.urls import path
from showapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
]
