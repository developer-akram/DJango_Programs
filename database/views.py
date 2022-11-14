from django.shortcuts import render,redirect
from .models import StudentNew, StudentRegistration
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

def adddata(request):
    if request.method =='POST':
        rno = request.POST['rno']
        name = request.POST['name']
        branch = request.POST['branch']
        fees = request.POST['fees']
        obj = StudentNew(rno=rno, name=name, branch=branch, fees=fees)
        obj.save()
        return render(request, 'database/adddata.html',{'key':'Student Data Submitted Successfully'})
    return render(request, 'database/adddata.html')

def applyform(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        email = request.POST['email']
        mobile = request.POST['mobile']
        country = request.POST['country']
        state = request.POST.getlist('state')
        states = ''
        for i in range(len(state)):
            if state[i] == '':
                continue
            if i == len(state) - 1:
                states += state[i]
            else:
                states += state[i] + ', '
        city = request.POST['city']
        qualification = request.POST['qualification']
        course = request.POST.getlist('tech')
        courses = ''
        for i in range(len(course)):
            if course[i] == '':
                continue
            if i == len(course) - 1:
                courses += course[i]
            else:
                courses += course[i] + ', '
        message = request.POST['txtarea']
        newobj = StudentRegistration(name = name, gender = gender, email = email, mobile = mobile, country = country, states = states, city = city, qualification = qualification, courses = courses, message = message)
        newobj.save()
        return redirect('viewform')
        #return render(request, 'database/applyform.html',{'applytrue':'Your Form has been Successfully Submitted, Thank You.'})
    return render(request, 'database/applyform.html')

def viewform(request):
    viewAllData = StudentRegistration.objects.all()
    return render(request, 'database/viewform.html',{'all':viewAllData})

def deleteform(request):
    data = StudentRegistration.objects.get(pk = request.GET['q'])
    if request.method == 'POST':
        data.delete()
        return redirect('viewform')
    return render(request, 'database/deleteform.html',{'id':data})

def correctionform(request):
    data = StudentRegistration.objects.get(pk = request.GET['q'])
    if request.method == 'POST':
        data.name = request.POST['name']
        data.gender = request.POST['gender']
        data.email = request.POST['email']
        data.mobile = request.POST['mobile']
        data.country = request.POST['country']
        state = request.POST.getlist('state')
        data.states = ''
        for i in range(len(state)):
            if state[i] == '':
                continue
            if i == len(state) - 1:
                data.states += state[i]
            else:
                data.states += state[i] + ', '
        data.city = request.POST['city']
        data.qualification = request.POST['qualification']
        course = request.POST.getlist('tech')
        data.courses = ''
        for i in range(len(course)):
            if course[i] == '':
                continue
            if i == len(course) - 1:
                data.courses += course[i]
            else:
                data.courses += course[i] + ', '
        data.message = request.POST['txtarea']
        data.save()
        return redirect('viewform')
    return render(request, 'database/correctionform.html',{'cor':data})

# Create your views here.
