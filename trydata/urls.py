from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),
    path('addnew',views.addnew,name='addnew'),
    path('showdata',views.showdata,name='showdata'),
    path('updatedata',views.updatedata,name='updatedata'),
    path('deletedata',views.deletedata,name='deletedata'),
]