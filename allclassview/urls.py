from django.urls import path
from allclassview.views import *

urlpatterns = [
    path('',JobCreate.as_view()),
    path('joblist',JobList.as_view()),
    path('<pk>',JobDetail.as_view()),
    path('<pk>/jupdate',JobUpdate.as_view()),
     path('<pk>/jdelete',JobDelete.as_view())
]