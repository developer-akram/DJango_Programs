from django.urls import path
from .import views

urlpatterns = [
    path('',views.getcook,name='getcook'),
]