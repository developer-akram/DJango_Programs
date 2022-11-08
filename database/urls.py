from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dataadd',views.dataadd,name="dataadd"),
    path('update',views.update,name="update"),
    path('registration',views.registration,name="registration"),
    path('viewdata',views.viewdata,name="viewdata"),
    path('deleteData',views.deleteData,name="deleteData"),
]