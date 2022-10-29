from django.urls import path
from .import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('feature',views.feature,name='feature'),
    path('team',views.team,name='team'),
    path('course',views.course,name='course'),
    path('detail',views.detail,name='detail'),
    path('testimonial',views.testimonial,name='testimonial'),
]