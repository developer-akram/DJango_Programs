import re
from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return render(request, 'first.html')
def second(request):
    a = request.GET.get('name1')
    return render(request, 'second.html',{'key':a})
def third(request):
    if request.GET.get('revname') != 'reverse':
        a = request.GET.get('name') 
        a = a + ' ' + request.GET.get('name2')
        return render(request, 'third.html',{'key':a})
    else:
        a = request.GET.get('name')
        return render(request, 'first.html',{'key':a})
def rev(request):
    a = request.GET.get('name')
    a = a + ' ' +  request.GET.get('name3')
    return render(request, 'second.html',{'revkey':'reverse','key':a})
# Create your views here.
