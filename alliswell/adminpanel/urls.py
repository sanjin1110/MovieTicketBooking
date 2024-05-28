from django.urls import path,include
from adminpanel import views

urlpatterns = [
    path('',views.adminlogin),
    
]