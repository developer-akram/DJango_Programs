from django .urls import path
from classView.views import *

urlpatterns = [
    path('',Addition.as_view()),
]