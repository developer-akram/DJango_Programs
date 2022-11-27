from django.urls import path
from .import views

urlpatterns = [
    path('',views.setcook,name='setcook'),
]