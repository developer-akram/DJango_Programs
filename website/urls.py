from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('findstu',views.findstu,name='findstu'),
    path('deletestu',views.deletestu,name='deletestu'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]