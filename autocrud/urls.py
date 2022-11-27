from django.urls import path
from autocrud.views import * 

urlpatterns = [
    path('',EmpCreate.as_view()),
    path('emplist',EmpList.as_view()),
    path('<pk>',EmpDetail.as_view()),
    path('<pk>/empupdate',EmpUpdate.as_view()),
    path('<pk>/empdelete',EmpDelete.as_view()),
]