from django.shortcuts import render,redirect
from .models import StudentNew
def index(request):
    return render(request, 'database/index.html')

def dataadd(request):
    return render(request, 'database/dataadd.html')

def update(request):
    data = StudentNew.objects.get(pk=request.GET["q"])
    if request.method == 'POST':
        data.rno = request.POST['rno']
        data.name = request.POST['name']
        data.branch = request.POST['branch']
        data.fees = request.POST['fees']
        data.save()
        return redirect('viewdata')
    return render(request, 'database/update.html',{'student':data})

def deleteData(request):
    data = StudentNew.objects.get(pk=request.GET["q"])
    data.delete()
    return redirect('viewdata')
def viewdata(request):
    data = StudentNew.objects.all()
    return render(request, 'database/viewdata.html',{'viewData':data})

def registration(request):
    if request.method =='POST':
        rno = request.POST['rno']
        name = request.POST['name']
        branch = request.POST['branch']
        fees = request.POST['fees']
        obj = StudentNew(rno=rno, name=name, branch=branch, fees=fees)
        obj.save()
        return render(request, 'database/registration.html',{'key':'Student Data Submitted Successfully'})
    return render(request, 'database/registration.html')

# Create your views here.
