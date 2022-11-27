from django.urls import path
from .import views

urlpatterns = [
    path('getcookie',views.getcookie,name='getcookie'),
    path('',views.setcookie,name='setcookie'),
    path('login',views.login,name='login'),
]