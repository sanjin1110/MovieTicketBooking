from django.urls import path,include
from theatre import views

urlpatterns = [
    path('',views.TheatreListView.as_view()),
    
]