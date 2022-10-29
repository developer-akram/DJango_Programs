from django.urls import path
from .import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('service',views.service,name='service'),
    path('blog',views.blog,name='blog'),
    path('team',views.team,name='team'),
    path('detail',views.detail,name='detail'),
    path('testimonial',views.testimonial,name='testimonial'),
]