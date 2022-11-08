from django.shortcuts import render

def index(request):
    return render(request, 'trydata/index.html')

def showdata(request):
    return render(request, 'trydata/showdata.html')

def addnew(request):
    return render(request, 'trydata/addnew.html')

def updatedata(request):
    return render(request, 'trydata/updatedata.html')


# Create your views here.
