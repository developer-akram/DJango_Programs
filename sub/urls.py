from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('input/', views.u_input, name='u_input'),
]