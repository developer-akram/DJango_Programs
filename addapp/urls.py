from django.urls import path
from addapp.views import Add,Prime,JobCreate,JobList

urlpatterns = [
    path('',Add.as_view()),
    path('prime',Prime.as_view()),
    path('job',JobCreate.as_view()),
    path('joblist',JobList.as_view())
]