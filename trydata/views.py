from django.shortcuts import render, redirect
from .models import MyStudent

def index(request):
    return render(request, 'trydata/index.html')

def showdata(request):
    data = MyStudent.objects.all()
    return render(request, 'trydata/showdata.html',{'show':data})

def addnew(request):
    if request.method == 'POST':
        roll = request.POST['sroll']
        name = request.POST['sname']
        branch = request.POST['sbranch']
        fees = request.POST['sfees']
        data = MyStudent(roll = roll, name = name, branch = branch, fees = fees)
        data.save()
        return render(request, 'trydata/addnew.html',{'save':'Data Records save successfully'})
    return render(request, 'trydata/addnew.html')

def deletedata(request):
    x = MyStudent.objects.get(pk = request.GET['q'])
    x.delete()
    return redirect('showdata')
def updatedata(request):
    data = MyStudent.objects.get(pk = request.GET['q'])
    if request.method == 'POST':
        data.roll = request.POST['sroll']
        data.name = request.POST['sname']
        data.branch = request.POST['sbranch']
        data.fees = request.POST['sfees']
        data.save()
        return redirect('showdata')
    return render(request, 'trydata/updatedata.html',{'stu':data})


# Create your views here.
