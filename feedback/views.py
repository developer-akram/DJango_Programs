from django.shortcuts import render,redirect
from .models import StudentNew, StudentRegistration,User,Courses,Faculty,Student
from django.db.models import Avg


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        obj = User(username = username, password = password, email = email, mobile_no = mobile_no)
        obj.save()
        return render(request, 'feedback/index.html',{"key":"Successfully Registered"})
    return render(request, 'feedback/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        obj = User.objects.filter(username = username, password = password)
        if obj.count()== 1:
            return redirect('viewform')
        else:
            return render(request, 'feedback/login.html',{'key':'Invalid username or password'})
    return render(request, 'feedback/login.html')

def dataadd(request):
    return render(request, 'feedback/dataadd.html')

def update(request):
    data = StudentNew.objects.get(pk=request.GET["q"])
    if request.method == 'POST':
        data.rno = request.POST['rno']
        data.name = request.POST['name']
        data.branch = request.POST['branch']
        data.fees = request.POST['fees']
        data.save()
        return redirect('viewdata')
    return render(request, 'feedback/update.html',{'student':data})

def deleteData(request):
    data = StudentNew.objects.get(pk=request.GET["q"])
    data.delete()
    return redirect('viewdata')
def viewdata(request):
    data = StudentNew.objects.all()
    return render(request, 'feedback/viewdata.html',{'viewData':data})

def adddata(request):
    if request.method =='POST':
        rno = request.POST['rno']
        name = request.POST['name']
        branch = request.POST['branch']
        fees = request.POST['fees']
        obj = StudentNew(rno=rno, name=name, branch=branch, fees=fees)
        obj.save()
        return render(request, 'feedback/adddata.html',{'key':'Student Data Submitted Successfully'})
    return render(request, 'feedback/adddata.html')

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
        #return render(request, 'feedback/applyform.html',{'applytrue':'Your Form has been Successfully Submitted, Thank You.'})
    return render(request, 'feedback/applyform.html')

def viewform(request):
    viewAllData = StudentRegistration.objects.all()
    return render(request, 'feedback/viewform.html',{'all':viewAllData})

def deleteform(request):
    data = StudentRegistration.objects.get(pk = request.GET['q'])
    if request.method == 'POST':
        data.delete()
        return redirect('viewform')
    return render(request, 'feedback/deleteform.html',{'id':data})

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
    return render(request, 'feedback/correctionform.html',{'cor':data})

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        f_name = Faculty.objects.filter(name = name) 
        students = Student.objects.filter(faculty__name = name)
        avg = students.aggregate(Avg('rating'))
        return render(request, 'feedback/feedback.html',{'name':f_name,'student':students,'avg':avg})
        
    return render(request, 'feedback/feedback.html')

# Create your views here.
