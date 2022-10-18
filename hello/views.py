from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = {'fname':'Akram','lname':'Khan'}
    return render(request, 'index.html',a)
    # return HttpResponse("Hello World")

# Create your views here.
