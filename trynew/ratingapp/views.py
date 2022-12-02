from django.shortcuts import render
from django.http import HttpResponse
from ratingapp.models import *
def index(request):
    c_list = Course.objects.all()
    f_list = Faculty.objects.filter(course__name = 'Python')
    return render(request, 'ratingapp/index.html',{'courses':c_list,'faculty':f_list})

# Create your views here.
