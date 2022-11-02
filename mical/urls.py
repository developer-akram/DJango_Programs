from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('furnitures',views.furnitures,name='furnitures'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('contacts',views.contacts,name='contacts')
]